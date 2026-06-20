import pygame
from color_file import Colors

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Blocks:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move_block(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
