import random
import pygame
from grid_file import Grid
from blocks_file import LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock

class Game:
    def __init__(self):
        self._grid = Grid()
        self._current_block = self.get_random_block()
        self._next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def get_random_block(self):
        blocks_pool = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        return random.choice(blocks_pool)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points