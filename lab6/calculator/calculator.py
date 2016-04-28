#!/usr/bin/env python3
# coding: utf-8
# Lab 6 - Calculator
# François Chalifour

import os
from collections import OrderedDict


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class History:
    """
    Manages the history of the calculator
    """
    def __init__(self):
        self.values = []


    def __repr__(self):
        return '{:d} is stored in memory.'.format(self.get_last_value())


    def get_last_value(self):
        return self.values[-1] if len(self.values) > 0 else None


    def add(self, value):
        self.values.append(value)


    def undo(self):
        if len(self.values) > 1:
            self.values.pop()
            return True
        else:
            return False


    def clear(self):
        self.values.clear()


class Storage:
    """
    Manages the storage of the calculator
    Stores and loads the values
    """
    def __init__(self, history):
        self.STORE_FILE = 'history.log'
        self.history = history


    def store(self):
        history_values = ' '.join([ str(x) for x in self.history.values ])
        try:
            with open(os.path.join(__location__, self.STORE_FILE), 'w') as history_file:
                history_file.write(history_values)
        except:
            return False
        else:
            return True


    def load(self):
        try:
            with open(os.path.join(__location__, self.STORE_FILE), 'r') as history_file:
                history_line = history_file.readline().split()
                if len(history_line) == 0:
                    raise(FileNotFoundError)
        except FileNotFoundError:
            return False
        else:
            self.history.clear()
            for x in history_line:
                if x != ' ':
                    self.history.add(int(x))
            return True


class Calculator:
    """
    Manages the calculator program
    """
    def __init__(self):
        self.commands = OrderedDict([
            ('add', lambda val, op: val + op),
            ('sub', lambda val, op: val - op),
            ('mul', lambda val, op: val * op),
            ('div', lambda val, op: val // op),
            ('undo', ''),
            ('store', ''),
            ('load', ''),
            ('quit', '')
        ])
        self.running = True
        self.history = History()
        self.storage = Storage(self.history)


    def print_title(self):
        print('''
        ======================
              CALCULATOR
        ======================
        ''')


    def ask_initial_value(self):
        while True:
            try:
                value = int(input('Enter initial memory value: '))
            except ValueError:
                print('Number expected')
            else:
                return value


    def ask_operation(self):
        while True:
            operation = input('Enter operation ({}): '.format('/'.join(self.commands.keys())))
            if operation in self.commands:
                return operation


    def ask_operand(self, operation):
        while True:
            try:
                operand = int(input('Enter operand: '))
            except ValueError:
                print('Number expected')
            else:
                if operation.startswith('div') and operand == 0:
                    print('Division by zero forbidden')
                else:
                    return operand


    def quit(self):
        self.running = False


    def run_action(self, operation):
        if operation.startswith('quit'):
            self.quit()
        elif operation.startswith('undo'):
            if self.history.undo():
                print(self.history)
            else:
                print('There\'s nothing to undo.')
        elif operation.startswith('store'):
            if self.storage.store():
                print('The state of the calculator has been stored.')
            else:
                print('The state could not be stored.')
        elif operation.startswith('load'):
            if self.storage.load():
                print('The state of the calculator has been loaded.')
                print(self.history)
            else:
                print('The history is empty, no state to load.')
        else:
            operand = self.ask_operand(operation)
            value = self.commands[operation](self.history.get_last_value(), operand)
            self.history.add(value)
            print(self.history)


    def launch(self):
        self.print_title()

        value = self.ask_initial_value()
        self.history.add(value)

        while self.running:
            operation = self.ask_operation()
            self.run_action(operation)

        print('The program finished with {:d} in memory.'.format(self.history.get_last_value()))
        return value


if __name__ == '__main__':
    calculator = Calculator()
    calculator.launch()
