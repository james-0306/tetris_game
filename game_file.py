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