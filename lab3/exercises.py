#!/usr/bin/env python3
# coding: utf-8
# Lab 3 - Lists
# François Chalifour

from functools import reduce

def highest(numbers):
    """Returns the highest number in a given list"""
    return max(numbers) if numbers else None


def count(numbers):
    """Returns a list of integers representing the number of times that the
    index appears as a value in the received list"""
    return [ numbers.count(x) for x in range(highest(numbers) + 1) ]


def are_equal(list1, list2):
    """Returns True if the numbers at each index in the two given lists are
    equal, otherwise False"""
    if len(list1) != len(list2): return False
    return all([ a == b for a, b in zip(list1, list2) ])


def are_nested_lists_equal(lists):
    """Returns True if all the nested lists are equal, otherwise False"""
    return all([ are_equal(lists[0], sublist) for sublist in lists ])


def change_to_highest(the_list):
    """Changes the received list so it contains the highest values from the
    nested lists"""
    the_list[:] = [ highest(x) for x in the_list ]


def sort(array):
    """Returns a new list where the numbers appear in increasing order"""
    sorted_array = list(array)
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if (sorted_array[j] > sorted_array[j + 1]):
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
    return sorted_array


def power_set(full_set):
    """Returns a list containing all the subsets of that set"""
    return reduce(lambda result, x: result + [ subset + [x] for subset in result ], full_set, [[]])


def test(got, expected):
    """Prints the actual result and the expected"""
    prefix = '[OK]' if got == expected else '[X]'
    print('{:5} got: {!r}'.format(prefix, got))
    print('      expected: {!r}'.format(expected))


def main():
    """Tests all the functions"""
    print('''
    ======================
            LAB 3
    ======================
    ''')

    print('1. Finding the highest value')
    test(highest([5, 3]), 5)
    test(highest([2, 8, 4, 3]), 8)
    test(highest([-2, -5]), -2)
    test(highest([]), None)

    print('\n2. Counting occurrences')
    test(count([0, 1, 2]), [1, 1, 1])
    test(count([1, 1, 1]), [0, 3])
    test(count([5, 2, 4, 7, 4]), [0, 0, 1, 0, 2, 1, 0, 1])

    print('\n3. Comparing two lists')
    test(are_equal([1, 2, 3], [1, 2, 3]), True)
    test(are_equal([2, 1, 3], [1, 2, 3]), False)
    test(are_equal([1, 2, 3], [1, 2, 2]), False)
    test(are_equal([1, 2, 3], [1, 2]), False)
    test(are_equal([1, 2], [1, 2, 3]), False)

    print('\n4. Comparing many lists')
    test(are_nested_lists_equal([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), True)
    test(are_nested_lists_equal([[1, 2, 3], [1, 2, 2], [1, 2, 3]]), False)
    test(are_nested_lists_equal([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), False)

    print('\n5. Populate the first list')
    the_list = [
        [1, 2, 3],
        [5, 4, 3],
        [2, 7, 6]
    ]
    test(change_to_highest(the_list), None)
    test(the_list, [3, 5, 7])

    print('\n6. A less simple calculator')
    print('See calculator.py')

    print('\n7. Sorting')
    test(sort([1, 4, 3, 2]), [1, 2, 3, 4])
    test(sort([9, 0, -1, 8]), [-1, 0, 8, 9])
    test(sort([1, 7, -1, -7]), [-7, -1, 1, 7])

    print('\n8. Power set')
    test(power_set([]), [[]])
    test(power_set([1]), [[], [1]])
    test(power_set([1, 2]), [[], [1], [2], [1, 2]])
    test(power_set([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


if __name__ == '__main__':
    main()
