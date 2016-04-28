#!/usr/bin/env python3
# coding: utf-8
# Lab 4 - Five in a row launcher
# François Chalifour

import five_in_a_row as five

game = {
    'width': 10,
    'height': 10,
    'moves': []
}

while five.get_winner(game) == None:
    five.print_game(game)

    next_player = five.get_next_players_turn(game)

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
            if not five.does_cell_exist(game, x, y):
                print('No cell with the coordinates x={} y={} exists, try again!'.format(x, y))
            elif not five.is_cell_free(game, x, y):
                print('The cell with the coordinates x={} y={} is not free, try again!'.format(x, y))
            else:
                are_entered_coordinates_ok = True

    five.make_move(game, x, y, next_player)

five.print_game(game)
print('The game is over, and the winner is: {}.'.format(five.get_winner(game)))
