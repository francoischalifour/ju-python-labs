#!/usr/bin/env python3
# coding: utf-8
# Lab 4 - Five in a row
# François Chalifour

def print_game(game):
    """
    Prints the game to the console.
    """
    print(' y')

    y = game['height'] - 1

    while 0 <= y:
        print('{}|'.format(y), end='')

        for x in range(game['width']):
            print(get_cell_value(game, x, y), end='')
        print()

        y -= 1

    print('-+', end='')
    for x in range(game['width']):
        print('-', end='')
    print('x')
    print(' |', end='')
    for x in range(game['width']):
        print(x, end='')
    print(' ')


def get_cell_value(game, x, y):
    """
    Returns 'X' if a cross has been placed in the cell with the given
    coordinates.
    Returns 'O' if a circle has been placed in the cell with the given
    coordinates.
    Returns ' ' otherwise.
    """
    moves = game.get('moves')
    for move in moves:
        if move.get('x') == x and move.get('y') == y:
            return move.get('player')
    return ' '


def make_move(game, x, y, player):
    """
    Adds a new move to the game with the information in the parameters.
    """
    new_move = {'x': x, 'y': y, 'player': player}
    game.get('moves').append(new_move)


def does_cell_exist(game, x, y):
    """
    Returns True if the game contains a cell with the given coordinates.
    Returns False otherwise.
    """
    return 0 <= x and x < game.get('width') and 0 <= y and y < game.get('height')


def is_cell_free(game, x, y):
    """
    Returns True if the cell at the given coordinates doesn't contain a cross
    or a circle.
    Returns False otherwise.
    """
    moves = game.get('moves')
    for move in moves:
        if move.get('x') == x and move.get('y') == y:
            return False
    return True


def get_next_players_turn(game):
    """
    Returns 'X' if a cross should be placed on the board next.
    Returns 'O' if a circle should be placed on the board next.
    """
    if len(game.get('moves')) == 0: return 'X'
    last_player = game.get('moves')[-1].get('player')
    return 'X' if last_player == 'O' else 'O'


def has_won_horizontal(game):
    """
    Returns 'X' if 5 crosses in a row is found in the game.
    Returns 'O' if 5 circles in a row is found in the game.
    Returns None otherwise.
    """
    for y in range(game.get('height')):
        for x in range(game.get('width') - 4):
            player = get_cell_value(game, x, y)
            if player != ' ':
                is_same_player = True
                for dx in range(1, 5):
                    if get_cell_value(game, x + dx, y) != player:
                        is_same_player = False
                        break
                if is_same_player:
                    return player
    return None


def has_won_vertical(game):
    """
    Returns 'X' if 5 crosses in a row is found in a col of the game.
    Returns 'O' if 5 circles in a row is found in a col of the game.
    Returns None otherwise.
    """
    for x in range(game.get('height')):
        for y in range(game.get('width') - 4):
            player = get_cell_value(game, x, y)
            if player != ' ':
                is_same_player = True
                for dy in range(1, 5):
                    if get_cell_value(game, x, y + dy) != player:
                        is_same_player = False
                        break
                if is_same_player:
                    return player
    return None


def has_won_diagonal(game):
    """
    Returns 'X' if 5 crosses in a row is found in a diagonal of the game.
    Returns 'O' if 5 circles in a row is found in a diagonal of the game.
    Returns None otherwise.
    """
    def get_diagonal(m, x, y, d):
        return [ m[(x + i - 1) % len(m)][(y + d * i - 1) % len(m[0])] for i in range(len(m)) ]

    moves = game.get('moves')
    board = [ [' ' for x in range(game.get('width'))] for x in range(game.get('height')) ]

    # Fill the game board
    for move in moves:
        board[move.get('x')][move.get('y')] = move.get('player')

    # Fill the diagonal board
    diagonals = [ get_diagonal(board, i, 1, 1) for i in range(1, game.get('width') + 1) ]
    diagonals_inversed = [ get_diagonal(board, 1, i, -1) for i in range(1, game.get('width') + 1) ]

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


def get_winner(game):
    """
    Returns 'X' if the X player wins.
    Returns 'O' if the O player wins.
    Returns None otherwise.
    """
    winner = has_won_horizontal(game)

    if not winner:
        winner = has_won_vertical(game)

    if not winner:
        winner = has_won_diagonal(game)

    return winner
