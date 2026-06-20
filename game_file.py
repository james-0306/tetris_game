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

    def move_left(self):
        self._current_block.move_block(0, -1)
        if not self.block_inside() or not self.block_fits():
            self._current_block.move_block(0, 1)

    def move_right(self):
        self._current_block.move_block(0, 1)
        if not self.block_inside() or not self.block_fits():
            self._current_block.move_block(0, -1)

    def move_down(self):
        self._current_block.move_block(1, 0)
        if not self.block_inside() or not self.block_fits():
            self._current_block.move_block(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self._current_block.get_cell_positions()
        for position in tiles:
            self._grid.grid[position.row][position.column] = self._current_block.id
        self._current_block = self._next_block
        self._next_block = self.get_random_block()
        rows_cleared = self._grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True
            
    def reset_game(self):
        self._grid.reset_grid()
        self._current_block = self.get_random_block()
        self._next_block = self.get_random_block()
        self.score = 0
        self.game_over = False

    def block_fits(self):
        tiles = self._current_block.get_cell_positions()
        for tile in tiles:
            if not self._grid.is_empty(tile.row, tile.column):
                return False
        return True

