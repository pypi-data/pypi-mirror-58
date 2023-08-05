import logging
import time
from typing import Dict, Callable

import pandas as pd
import json
import os

from google.protobuf.json_format import _Printer
from .utils.json_encoder import CarballJsonEncoder

script_path = os.path.abspath(__file__)
with open(os.path.join(os.path.dirname(script_path), 'PROTOBUF_VERSION'), 'r') as f:
    PROTOBUF_VERSION = json.loads(f.read())

from ..analysis.cleaner.cleaner import clean_replay
from ..analysis.saltie_game.metadata.ApiGame import ApiGame
from ..analysis.saltie_game.metadata.ApiMutators import ApiMutators
from ..analysis.saltie_game.metadata.ApiPlayer import ApiPlayer
from ..analysis.saltie_game.metadata.ApiTeam import ApiTeam
from ..analysis.saltie_game.saltie_game import SaltieGame
from ..analysis.stats.stats_manager import StatsManager
from ..analysis.utils.pandas_manager import PandasManager
from ..analysis.utils.proto_manager import ProtobufManager
from ..generated.api import game_pb2
from ..generated.api.player_pb2 import Player
from ..json_parser.game import Game
from ..analysis.events.event_creator import EventsCreator

logger = logging.getLogger(__name__)


class AnalysisManager:
    id_creator = None
    timer = None

    def __init__(self, game: Game):
        self.game = game
        self.protobuf_game = game_pb2.Game()
        self.protobuf_game.version = PROTOBUF_VERSION
        self.id_creator = self.create_player_id_function(game)
        self.stats_manager = StatsManager()
        self.events_creator = EventsCreator(self.id_creator)
        self.should_store_frames = False
        self.df_bytes = None

    def create_analysis(self, calculate_intensive_events: bool = False):
        """
        Organizes all the different analysis that can occurs.
        :param calculate_intensive_events: Indicates if expensive calculations should run to include additional stats.
        """
        self.start_time()
        player_map = self.get_game_metadata(self.game, self.protobuf_game)
        self.log_time("creating metadata")
        data_frame = self.get_data_frames(self.game)
        self.log_time("getting frames")
        kickoff_frames, first_touch_frames = self.get_kickoff_frames(self.game, self.protobuf_game, data_frame)
        self.game.kickoff_frames = kickoff_frames
        self.log_time("getting kickoff")
        if self.can_do_full_analysis(first_touch_frames):
            self.perform_full_analysis(self.game, self.protobuf_game, player_map,
                                       data_frame, kickoff_frames, first_touch_frames,
                                       calculate_intensive_events=calculate_intensive_events)
        else:
            self.protobuf_game.game_metadata.is_invalid_analysis = True

        # log before we add the dataframes
        # logger.debug(self.protobuf_game)

        self.store_frames(data_frame)

    def perform_full_analysis(self, game: Game, proto_game: game_pb2.Game, player_map: Dict[str, Player],
                              data_frame: pd.DataFrame, kickoff_frames: pd.DataFrame, first_touch_frames: pd.Series,
                              calculate_intensive_events: bool = False):

        """
        Performs the more in depth analysis on the game in addition to just metadata.
        :param game: Contains all metadata about the game and any json data.
        :param proto_game: The protobuf where all the stats are being stored.
        :param player_map: A map of player name to Player protobuf.
        :param data_frame: Contains the entire data from the game.
        :param kickoff_frames: Contains data about the kickoffs.
        :param first_touch_frames:  Contains data for frames where touches can actually occur.
        :param calculate_intensive_events: Indicates if expensive calculations should run to include additional stats.
        """
        self.get_game_time(proto_game, data_frame)
        clean_replay(game, data_frame, proto_game, player_map)
        self.events_creator.create_events(game, proto_game, player_map, data_frame, kickoff_frames, first_touch_frames,
            calculate_intensive_events=calculate_intensive_events)
        self.log_time("creating events")
        self.get_stats(game, proto_game, player_map, data_frame)

    def get_game_metadata(self, game: Game, proto_game: game_pb2.Game) -> Dict[str, Player]:

        # create general metadata
        ApiGame.create_from_game(proto_game.game_metadata, game, self.id_creator)

        # create team metadata
        ApiTeam.create_teams_from_game(game, proto_game, self.id_creator)

        ApiGame.create_parties(proto_game.parties, game, self.id_creator)
        # create player metadata
        player_map = dict()
        for player in game.players:
            player_proto = proto_game.players.add()
            ApiPlayer.create_from_player(player_proto, player, self.id_creator)
            player_map[str(player.online_id)] = player_proto

        # create mutators
        ApiMutators.create_from_game(proto_game.mutators, game, self.id_creator)

        return player_map

    def get_game_time(self, protobuf_game: game_pb2.Game, data_frame: pd.DataFrame):
        protobuf_game.game_metadata.length = data_frame.game[data_frame.game.goal_number.notnull()].delta.sum()
        for player in protobuf_game.players:
            try:
                player.time_in_game = data_frame[
                    data_frame[player.name].pos_x.notnull() & data_frame.game.goal_number.notnull()].game.delta.sum()
                player.first_frame_in_game = data_frame[player.name].pos_x.first_valid_index()
            except:
                player.time_in_game = 0
        logger.info('created all times for players')

    def get_data_frames(self, game: Game):
        data_frame = SaltieGame.create_data_df(game)

        logger.info("Assigned goal_number in .data_frame")
        return data_frame

    def get_kickoff_frames(self, game: Game, proto_game: game_pb2.Game, data_frame: pd.DataFrame):
        kickoff_frames = SaltieGame.get_kickoff_frames(game)
        first_touch_frames = SaltieGame.get_first_touch_frames(game)

        if len(kickoff_frames) > len(first_touch_frames):
            # happens when the game ends before anyone touches the ball at kickoff
            kickoff_frames = kickoff_frames[:len(first_touch_frames)]

        for goal_number, goal in enumerate(game.goals):
            data_frame.loc[
            kickoff_frames[goal_number]: goal.frame_number, ('game', 'goal_number')
            ] = goal_number

        # Set goal_number of frames that are post last kickoff to -1 (ie non None)
        if len(kickoff_frames) > len(proto_game.game_metadata.goals):
            data_frame.loc[kickoff_frames[-1]:, ('game', 'goal_number')] = -1

        for index in range(min(len(kickoff_frames), len(first_touch_frames))):
            kickoff = proto_game.game_stats.kickoffs.add()
            kickoff.start_frame_number = kickoff_frames[index]
            kickoff.end_frame_number = first_touch_frames[index]

        return kickoff_frames, first_touch_frames

    def get_stats(self, game: Game, proto_game: game_pb2.Game, player_map: Dict[str, Player],
                  data_frame: pd.DataFrame):
        """
        Calculates all stats that are beyond the basic event creation.
        This is only active on valid goal frames.
        """
        goal_frames = data_frame.game.goal_number.notnull()
        self.stats_manager.get_stats(game, proto_game, player_map, data_frame[goal_frames])

    def store_frames(self, data_frame: pd.DataFrame):
        self.data_frame = data_frame
        self.df_bytes = PandasManager.safe_write_pandas_to_memory(data_frame)

    def write_proto_out_to_file(self, file):
        ProtobufManager.write_proto_out_to_file(file, self.protobuf_game)

    def write_pandas_out_to_file(self, file):
        if self.df_bytes is not None:
            file.write(self.df_bytes)
        elif not self.should_store_frames:
            logger.warning("pd DataFrames are not being stored anywhere")

    def get_protobuf_data(self) -> game_pb2.Game:
        """
        :return: The protobuf data created by the analysis
        """
        return self.protobuf_game

    def get_data_frame(self) -> pd.DataFrame:
        return self.data_frame

    def start_time(self):
        self.timer = time.time()
        logger.info("starting timer")

    def log_time(self, message=""):
        end = time.time()
        logger.info("Time taken for %s is %s milliseconds", message, (end - self.timer) * 1000)
        self.timer = end

    def create_player_id_function(self, game: Game) -> Callable:
        name_map = {player.name: player.online_id for player in game.players}

        def create_name(proto_player_id, name):
            proto_player_id.id = str(name_map[name])

        return create_name

    def can_do_full_analysis(self, first_touch_frames) -> bool:
        # Analyse only if 1v1 or 2v2 or 3v3
        team_sizes = []
        for team in self.game.teams:
            team_sizes.append(len(team.players))

        if len(team_sizes) == 0:
            logger.warning("Not doing full analysis. No teams found")
            return False
        if len(first_touch_frames) == 0:
            logger.warning("Not doing full analysis. No one touched the ball")
            return False
        # if any((team_size != team_sizes[0]) for team_size in team_sizes):
        #     logger.warning("Not doing full analysis. Not all team sizes are equal")
        #     return False

        return True

    def write_json_out_to_file(self, file):
        printer = _Printer()
        js = printer._MessageToJsonObject(self.protobuf_game)
        json.dump(js, file, indent=2, cls=CarballJsonEncoder)
