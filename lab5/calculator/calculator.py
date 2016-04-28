#!/usr/bin/env python3
# coding: utf-8
# Lab 5 - Calculator
# François Chalifour

import os
from collections import OrderedDict


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_last_value(history):
    return history[-1] if len(history) > 0 else None


def undo(history):
    if len(history) > 1:
        history.pop()
        return True
    else:
        return False


def print_last_value(history):
    print('{:d} is stored in memory.'.format(get_last_value(history)))


def store(history, file):
    history_values = ' '.join([ str(x) for x in history ])
    try:
        with open(os.path.join(__location__, STORE_FILE), 'w') as history_file:
            history_file.write(history_values)
    except:
        return False
    else:
        return True


def load(history, file):
    try:
        with open(os.path.join(__location__, STORE_FILE), 'r') as history_file:
            history_line = history_file.readline().split()
            if len(history_line) == 0:
                raise(FileNotFoundError)
    except FileNotFoundError:
        print('The history is empty, no state to load.')
        return False
    else:
        history.clear()
        for x in history_line:
            if x != ' ':
                history.append(int(x))
        return True


def calculator():
    """Integers calculator with store and load operations"""
    print('''
    ======================
          CALCULATOR
    ======================
    ''')

    commands = OrderedDict([
        ('add', lambda val, op: val + op),
        ('sub', lambda val, op: val - op),
        ('mul', lambda val, op: val * op),
        ('div', lambda val, op: val // op),
        ('undo', ''),
        ('store', ''),
        ('load', ''),
        ('quit', '')
    ])
    history = []
    STORE_FILE = 'history.log'

    while True:
        try:
            value = int(input('Enter initial memory value: '))
        except ValueError:
            print('Number expected')
        else:
            history.append(value)
            break

    while True:
        while True:
            operation = input('Enter operation ({}): '.format('/'.join(commands.keys())))
            if operation in commands: break

        if operation.startswith('quit'): break
        elif operation.startswith('undo'):
            if undo(history):
                print_last_value(history)
            else:
                print('There\'s nothing to undo.')
        elif operation.startswith('store'):
            if store(history, STORE_FILE):
                print('The state of the calculator has been stored.')
            else:
                print('The state could not be stored.')
        elif operation.startswith('load'):
            if load(history, STORE_FILE):
                print('The state of the calculator has been loaded.')
                print_last_value(history)
            else:
                print('The history is empty, no state to load.')
        else:
            while True:
                try:
                    operand = int(input('Enter operand: '))
                except ValueError:
                    print('Number expected')
                else:
                    if operation.startswith('div') and operand == 0:
                        print('Division by zero forbidden')
                    else:
                        break

            value = commands[operation](value, operand)
            history.append(value)
            print_last_value(history)

    print('The program finished with {:d} in memory.'.format(get_last_value(history)))
    return value


if __name__ == '__main__':
    calculator()
