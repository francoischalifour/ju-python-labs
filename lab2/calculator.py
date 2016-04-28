#!/usr/bin/env python3
# coding: utf-8
# Lab 2 - Calculator
# François Chalifour

from collections import OrderedDict

def calculator():
    """Simple integers calculator"""
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
        ('quit', '')
    ])

    while True:
        try:
            value = int(input('Enter initial memory value: '))
            break
        except ValueError:
            print('Number expected')

    while True:
        while True:
            operation = input('Enter operation ({}): '.format('/'.join(commands.keys())))
            if operation in commands: break

        if operation.startswith('quit'): break

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
        print('{:d} is stored in memory.'.format(value))

    print('The program finished with {:d} in memory.'.format(value))
    return value


if __name__ == '__main__':
    calculator()
