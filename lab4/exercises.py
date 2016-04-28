#!/usr/bin/env python3
# coding: utf-8
# Lab 4 - Dictionaries
# François Chalifour

def sums(numbers):
    """Returns a dictionary where the key "odd" contains the sum of all the odd
    integers in the list, the key "even" contains the sum of all the even
    integers, and the key "all" contains the sum of all integers"""
    sums = {'odd': 0, 'even': 0, 'all': 0}
    for x in numbers:
        if x % 2 == 0:
            sums['even'] += x
        else:
            sums['odd'] += x
        sums['all'] += x
    return sums


def test(got, expected):
    """Prints the actual result and the expected"""
    prefix = '[OK]' if got == expected else '[X]'
    print('{:5} got: {!r}'.format(prefix, got))
    print('      expected: {!r}'.format(expected))


def main():
    """Tests all the functions"""
    print('''
    ======================
            LAB 4
    ======================
    ''')

    print('1. Computing sums')
    test(sums([1, 2, 3, 4, 5]), {"odd": 9, "even": 6, "all": 15})


if __name__ == '__main__':
    main()
