#!/usr/bin/env python3
# coding: utf-8
# Lab 2 - Basic functions
# François Chalifour

def abs(n=0):
    """Returns the absolute value of a given number"""
    return -n if n < 0 else n


def closest_to_zero(a=0, b=0):
    """Returns the closest number to 0 in the two given"""
    return min([a, b], key=abs)


def closest_to_zero_4(a, b, c, d):
    """Returns the closest number to 0 in the four given"""
    return min([a, b, c, d], key=abs)


def closest_to_zero_10(a, b, c, d, e, f, g, h, i, j):
    """Returns the closest number to 0 in the ten given"""
    return min([a, b, c, d, e, f, g, h, i, j], key=abs)


def closest_to_zero_all(array):
    """Returns the closest number to 0 in the given array"""
    return min(array, key=abs)


def string_with_numbers(n=1):
    """Returns a string containing all numbers until the given separated by an
     underscore"""
    return '_'.join([ str(x) for x in range(1, n + 1) ])


def test(got, expected):
    """Prints the actual result and the expected"""
    prefix = '[OK]' if got == expected else '[X]'
    print('{:5} got: {!r}'.format(prefix, got))
    print('      expected: {!r}'.format(expected))


def main():
    """Tests all the functions"""
    print('''
    ======================
            LAB 2
    ======================
    ''')

    print('1. Absolute value')
    test(abs(5), 5)
    test(abs(-5), 5)
    test(abs(0), 0)

    print('\n2. Closest to zero')
    test(closest_to_zero(5, 9), 5)
    test(closest_to_zero(3, -2), -2)
    test(closest_to_zero(2, 2), 2)

    print('\n3. Closest to zero (4 values)')
    test(closest_to_zero_4(5, 9, 2, 11), 2)
    test(closest_to_zero_4(0, 3, -2, 4), 0)
    test(closest_to_zero_4(2, 2, -2, 1), 1)

    print('\n4. Closest to zero (10 values)')
    test(closest_to_zero_10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1)

    print('\n4 (bis). Closest to zero (array)')
    test(closest_to_zero_all([5, 9]), 5)
    test(closest_to_zero_all([5, 9, 2, 11]), 2)
    test(closest_to_zero_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

    print('\n5. String with numbers')
    test(string_with_numbers(3), '1_2_3')
    test(string_with_numbers(5), '1_2_3_4_5')

    print('\n6. Calculator')
    print('See calculator.py')


if __name__ == '__main__':
    main()
