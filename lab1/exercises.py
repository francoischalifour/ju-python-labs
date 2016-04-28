#!/usr/bin/env python3
# coding: utf-8
# Lab 1 - Mathematical functions
# François Chalifour

def factorial(n=0):
    """Returns the factorial of a given integer"""
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)


def exp(n=1, e=0):
    """Returns the first argument to the power of the second"""
    if e == 0: return 1
    if e > 0: return n * exp(n, e - 1)
    if e < 0: return 1 / exp(n, -e)


def sum(n=1):
    """Returns the sum from 1 to a given integer times its own value"""
    if n == 1: return 1
    return n * n + sum(n - 1)


def sum_of_ints(a=0, b=0):
    """Returns the sum of the integers between the two given integers.
    The first integer should be smaller than the second"""
    if a > b: return 0
    return a + sum_of_ints(a + 1, b)


def combinations(n=0, k=0):
    """Given two integers (n and k), returns the number of combinations
    possible to create by picking k elements from n elements"""
    return factorial(n) // (factorial(k) * factorial(n - k))


def test(fn, *args):
    """Executes the given function with its parameters and prints the result"""
    params = ', '.join([ str(arg) for arg in args ])
    print('> {}({}) = {}'.format(fn.__name__, params, fn(*args)))


def main():
    """Tests all the functions"""
    print('''
    ======================
            LAB 1
    ======================
    ''')

    print('\t1. Factorial')
    test(factorial, 0)
    test(factorial, 7)

    print('\n\t2. Exponentiation')
    test(exp, *[5, 0])
    test(exp, *[2, 1])
    test(exp, *[2, 2])
    test(exp, *[2, 3])
    test(exp, *[2, -2])

    print('\n\t3. A different sum')
    test(sum, 1)
    test(sum, 2)
    test(sum, 3)
    test(sum, 4)

    print('\n\t4. Summering Integers')
    test(sum_of_ints, *[0, 4])
    test(sum_of_ints, *[10, 11])
    test(sum_of_ints, *[7, 7])
    test(sum_of_ints, *[-2, 2])
    test(sum_of_ints, *[-4, 0])

    print('\n\t5. Combinations')
    test(combinations, *[5, 0])
    test(combinations, *[5, 1])
    test(combinations, *[5, 2])
    test(combinations, *[5, 3])
    test(combinations, *[5, 4])
    test(combinations, *[5, 5])


if __name__ == '__main__':
    main()
