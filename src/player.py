from enum import Enum
from itertools import cycle
import random
from typing import Literal

PLAYER_IDX_TYPE = Literal[0, 1]

class BallState(Enum):
    LOSE = 'LOSE'
    CONTINUE = 'CONTINUE'

class Player:
    def __init__(self, name: str, continue_chance: int):
        self.name = name
        self.continue_chance = continue_chance


    def _hit_ball(self) -> BallState:
        return random.choices([BallState.CONTINUE, BallState.LOSE], weights=[self.continue_chance, 100 - self.continue_chance])[0]
    
class Match:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def _get_player_by_index(self, idx: PLAYER_IDX_TYPE) -> Player:
        players = [self.player1, self.player2]
        return players[idx]
    
    def _simulate_point(self, serve_player_idx: PLAYER_IDX_TYPE) -> PLAYER_IDX_TYPE:
        current_player_idx = serve_player_idx
        print(f"{self._get_player_by_index(current_player_idx).name} serves the ball")
        while True:
            current_player_idx = current_player_idx ^ 1
            current_player = self._get_player_by_index(current_player_idx)
            outcome = current_player._hit_ball()
            if outcome == BallState.LOSE:
                print(f"{current_player.name} loses the ball")
                winner_idx = current_player_idx ^ 1
                return winner_idx
            else:
                print(f"{current_player.name} hits the ball back")


    def _simulate_game(self, serve_player_idx: PLAYER_IDX_TYPE):
        score = [0, 0]
        while True:
            winner_idx = self._simulate_point(serve_player_idx=serve_player_idx)
            score[winner_idx] += 1
            if score[winner_idx] >= 4 and score[winner_idx] - score[winner_idx ^ 1] >= 2:
                winner_player = self._get_player_by_index(winner_idx)
                print("-"*20)
                print(f"{winner_player.name} won the game with {score}")
                return winner_idx
            
    def _simulate_match(self, win_games: int=3):
        match_score = [0, 0]
        current_serve_player_idx = 0
        while True:
            current_serve_player_idx = current_serve_player_idx ^ 1
            current_player = self._get_player_by_index(current_serve_player_idx)
            print(f"{current_player.name} start serving")
            winner_idx = self._simulate_game(
                serve_player_idx = current_serve_player_idx
                )
            match_score[winner_idx] += 1
            if match_score[winner_idx] >= win_games:
                winner_player = self._get_player_by_index(winner_idx)
                print("-"*20)
                print(f"{winner_player.name} won the match with {match_score}")
                return winner_idx