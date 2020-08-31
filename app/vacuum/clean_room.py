# coding=utf-8

from __future__ import print_function

from typing import List


class Bot:
    def __init__(self, row, column):
        self._row: int = row
        self._column: int = column

    def next_move(self, world):
        if world.is_cell_dirty(self._row, self._column):
            world.set_cell_state(self._row, self._column, '-')
            return "CLEAN"

        next_dirty_cell = world.next_dirty_cell(self._row, self._column)
        if next_dirty_cell[0] < self._row:
            self._row -= 1
            return "UP"
        if next_dirty_cell[0] > self._row:
            self._row += 1
            return "DOWN"
        if next_dirty_cell[1] < self._column:
            self._column -= 1
            return "LEFT"
        if next_dirty_cell[1] > self._column:
            self._column += 1
            return "RIGHT"

        return None


class World:

    def __init__(self):
        self._world = list()
        for i in range(5):
            self._world.append(list())
            for j in range(5):
                self._world[i].append('-')

    def world(self):
        return self._world

    def set_cell_state(self, row, column, state):
        assert state == '-' or state == 'd' or state == 'b'
        self._world[row][column] = state if state != 'b' else '-'

    def is_cell_dirty(self, row, column):
        return self._world[row][column] == 'd'

    def is_clean(self):
        is_clean = True
        for i in range(5):
            for j in range(5):
                is_clean = False if self._world[i][j] == 'd' else is_clean

        return is_clean

    def next_dirty_cell(self, row, column) -> (int, int):
        """
        return the position of next dirty cell to clean up
        with coordinate (X, Y) as tuple
        """
        raise NotImplementedError


def clean_room(room: List[str], vacuum_position: List[int]) -> List[str]:
    bot = Bot(int(vacuum_position[0]), int(vacuum_position[1]))
    board = World()

    i = 0
    for row_value in room:
        j = 0
        for val in row_value:
            board.set_cell_state(i, j, val)
            j += 1
        i += 1

    moves = []
    while board.is_clean() is False:
        move = bot.next_move(board)
        moves.append(move)

    return moves
