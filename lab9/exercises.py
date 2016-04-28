#!/usr/bin/env python3
# coding: utf-8
# Lab 9 - Functional Programming
# François Chalifour

from functools import reduce

def product_between(a=0, b=0):
    """Returns the product of the integers between these two numbers"""
    return reduce(lambda a, b: a * b, range(a, b + 1), 1)


def sum_of_numbers(numbers):
    """Returns the sum of all the numbers in the list"""
    return reduce(lambda a, b: a + b, numbers, 0)


def is_in_list(x, numbers):
    """Returns True if the list contains the number, otherwise False"""
    return any(filter(lambda n: n == x, numbers))


def count(numbers, x):
    """Returns the number of time the number occurs in the list"""
    return len(filter(lambda n: n == x, numbers))


def test(got, expected):
    """Prints the actual result and the expected"""
    prefix = '[OK]' if got == expected else '[X]'
    print('{:5} got: {!r}'.format(prefix, got))
    print('      expected: {!r}'.format(expected))


def main():
    """Tests all the functions"""
    print('''
    ======================
            LAB 9
    ======================
    ''')

    print('1. Multiplying values')
    test(product_between(0, 1), 0)
    test(product_between(1, 3), 6)
    test(product_between(10, 10), 10)
    test(product_between(5, 7), 210)

    print('\n2. Summarizing numbers in lists')
    test(sum_of_numbers([]), 0)
    test(sum_of_numbers([1, 1, 1]), 3)
    test(sum_of_numbers([3, 1, 2]), 6)

    print('\n3. Searching for a value in a list')
    test(is_in_list(1, []), False)
    test(is_in_list(3, [1, 2, 3, 4, 5]), True)
    test(is_in_list(7, [1, 2, 1, 2]), False)

    print('\n4. Counting elements in lists')
    test(count([], 4), 0)
    test(count([1, 2, 3, 4, 5], 3), 1)
    test(count([1, 1, 1], 1), 3)


if __name__ == '__main__':
    main()
