#!/usr/bin/env python3
# coding: utf-8
# Lab 4 - Five in a Row launcher
# François Chalifour

from five_in_a_row import Game

game = Game()

while game.get_winner() == None:
    # Print the game board.
    game.print_game()

    # Ask the user to enter coordinates.
    next_player = game.get_next_players_turn()

    print('Enter the x and y coordinate for the cell to place {} in.'.format(next_player))
    print('Separate the coordinates by space, e.g: 3 5')

    are_entered_coordinates_ok = False

    while not are_entered_coordinates_ok:
        coordinates_string = input()
        coordinates = coordinates_string.split(' ')

        try:
            x = int(coordinates[0])
            y = int(coordinates[1])
        except ValueError:
            print('Coordinates error, try again!')
        else:
            if not game.does_cell_exist(x, y):
                print('No cell with the coordinates x={} y={} exists, try again!'.format(x, y))
            elif not game.is_cell_free(x, y):
                print('The cell with the coordinates x={} y={} is not free, try again!'.format(x, y))
            else:
                are_entered_coordinates_ok = True

    game.make_move(x, y, next_player)

game.print_game()
print('The game is over, and the winner is: {}.'.format(game.get_winner()))
