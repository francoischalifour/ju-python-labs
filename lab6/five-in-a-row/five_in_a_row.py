#!/usr/bin/env python3
# coding: utf-8
# Lab 6 - Five in a Row
# François Chalifour

class Move:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player


    def __repr__(self):
        return '{} played [{}, {}]'.format(self.player, self.x, self.y)


class ListMoves:
    def __init__(self):
        self.history = []


    def __repr__(self):
        return '\n'.join([ str(turn) for turn in self.history ])


    def __call__(self):
        return self.history


    def add_move(self, move):
        self.history.append(move)


class Game:
    def __init__(self, width=10, height=10):
        self.needed_in_row = 5
        self.width = width
        self.height = height
        self.moves = ListMoves()


    def print_game(self):
        """
        Prints the game to the console.
        """
        print(' y')

        y = self.height - 1

        while 0 <= y:
            print('{}|'.format(y), end='')

            for x in range(self.width):
                print(self.get_cell_value(x, y), end='')
            print()

            y -= 1

        print('-+', end='')
        for x in range(self.width):
            print('-', end='')
        print(' x')
        print(' |', end='')
        for x in range(self.width):
            print(x, end='')
        print(' ')


    def get_cell_value(self, x, y):
        """
        Returns 'X' if a cross has been placed in the cell with the given
        coordinates.
        Returns 'O' if a circle has been placed in the cell with the given
        coordinates.
        Returns ' ' otherwise.
        """
        for move in self.moves():
            if move.x == x and move.y == y:
                return move.player
        return ' '


    def does_cell_exist(self, x, y):
        """
        Returns True if the game contains a cell with the given coordinates.
        Returns False otherwise.
        """
        return 0 <= x and x < self.width and 0 <= y and y < self.height


    def is_cell_free(self, x, y):
        """
        Returns True if the cell at the given coordinates doesn't contain a cross
        or a circle.
        Returns False otherwise.
        """
        for move in self.moves():
            if move.x == x and move.y == y:
                return False
        return True


    def make_move(self, x, y, player):
        """
        Adds a new move to the game with the information in the parameters.
        """
        self.moves.add_move(Move(x, y, player))


    def get_next_players_turn(self):
        """
        Returns 'X' if a cross should be placed on the board next.
        Returns 'O' if a circle should be placed on the board next.
        """
        if len(self.moves()) == 0: return 'X'
        last_player = self.moves()[-1].player
        return 'X' if last_player == 'O' else 'O'


    def has_won_horizontal(self):
        """
        Returns 'X' if 5 crosses in a row is found in the game.
        Returns 'O' if 5 circles in a row is found in the game.
        Returns None otherwise.
        """
        for y in range(self.height):
            for x in range(self.width - (self.needed_in_row - 1)):
                player = self.get_cell_value(x, y)
                if player != ' ':
                    is_same_player = True
                    for dx in range(1, self.needed_in_row):
                        if self.get_cell_value(x + dx, y) != player:
                            is_same_player = False
                            break
                    if is_same_player:
                        return player
        return None


    def has_won_vertical(self):
        """
        Returns 'X' if 5 crosses in a row is found in a col of the game.
        Returns 'O' if 5 circles in a row is found in a col of the game.
        Returns None otherwise.
        """
        for x in range(self.height):
            for y in range(self.width - (self.needed_in_row - 1)):
                player = self.get_cell_value(x, y)
                if player != ' ':
                    is_same_player = True
                    for dy in range(1, self.needed_in_row):
                        if self.get_cell_value(x, y + dy) != player:
                            is_same_player = False
                            break
                    if is_same_player:
                        return player
        return None


    def has_won_diagonal(self):
        """
        Returns 'X' if 5 crosses in a row is found in a diagonal of the game.
        Returns 'O' if 5 circles in a row is found in a diagonal of the game.
        Returns None otherwise.
        """
        def get_diagonal(m, x, y, d):
            return [ m[(x + i - 1) % len(m)][(y + d * i - 1) % len(m[0])] for i in range(len(m)) ]

        board = [ [' ' for x in range(self.width)] for x in range(self.height) ]

        # Fill the game board
        for move in self.moves():
            board[move.x][move.y] = move.player

        # Fill the diagonal board
        diagonals = [ get_diagonal(board, i, 1, 1) for i in range(1, self.width + 1) ]
        diagonals_inversed = [ get_diagonal(board, 1, i, -1) for i in range(1, self.width + 1) ]

        for diagonal in diagonals:
            last_player = None
            count = 1
            for player in diagonal:
                if player != ' ' and player == last_player: count += 1
                last_player = player
                if count >= 5: return player

        for diagonal in diagonals_inversed:
            last_player = None
            count = 1
            for player in diagonal:
                if player != ' ' and player == last_player: count += 1
                last_player = player
                if count >= 5: return player

        return None


    def get_winner(self):
        """
        Returns 'X' if the X player wins.
        Returns 'O' if the O player wins.
        Returns None otherwise.
        """
        winner = self.has_won_horizontal()

        if not winner:
            winner = self.has_won_vertical()

        if not winner:
            winner = self.has_won_diagonal()

        return winner
