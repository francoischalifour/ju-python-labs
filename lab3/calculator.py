#!/usr/bin/env python3
# coding: utf-8
# Lab 3 - Calculator
# François Chalifour

from collections import OrderedDict

def undo(history):
    if len(history) > 1:
        history.pop()
        return True
    else:
        return False


def calculator():
    """Integers calculator with undo operation"""
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
        ('quit', '')
    ])
    history = []

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
        if operation.startswith('undo'):
            if not undo(history):
                print('There\'s nothing to undo.')
                continue
        else:
            while True:
                try:
                    operand = int(input('Enter operand: '))
                except ValueError:
                    print('Number expected')
                else:
                    if operation.startswith('div') and operand == 0:
                        print('Division by zero forbidden')
                    else: break

            value = commands[operation](value, operand)
            history.append(value)

        print('{:d} is stored in memory.'.format(history[-1]))

    print('The program finished with {:d} in memory.'.format(history[-1]))
    return value


if __name__ == '__main__':
    calculator()
