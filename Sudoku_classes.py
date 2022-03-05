import random
import math


class Sudoku:
    """The Main Application"""
    #main: Board[Board]

    def __init__(self) -> None:
        self.main = None

    def make_board(self):
        self.main = Board()
        for row in self.main.board:
            for col in self.main.board:
                self.main.board[row][col] = Board

    def del_board(self):
        self.main = None

    def randomize_solution(self):
        raise NotImplementedError


class Board:
    def __init__(self):
        self.board = [[0, 0, 0]
                      [0, 0, 0]
                      [0, 0, 0]]



s = Sudoku
s.make_board()
