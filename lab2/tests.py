#!/usr/bin/env python3
# coding: utf-8
# Lab 2 - Unit tests
# François Chalifour

import unittest
from exercises import *

class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        got = abs(5)
        expected = 5
        self.assertEqual(got, expected)

    def test_abs_minus_5(self):
        got = abs(-5)
        expected = 5
        self.assertEqual(got, expected)

    def test_abs_0(self):
        got = abs(0)
        expected = 0
        self.assertEqual(got, expected)

    def test_abs_empty(self):
        got = abs()
        expected = 0
        self.assertEqual(got, expected)


class TestClosestToZero(unittest.TestCase):
    def test_closest_5_9(self):
        got = closest_to_zero(5, 9)
        expected = 5
        self.assertEqual(got, expected)

    def test_closest_3_minus_2(self):
        got = closest_to_zero(3, -2)
        expected = -2
        self.assertEqual(got, expected)

    def test_closest_2_2(self):
        got = closest_to_zero(2, 2)
        expected = 2
        self.assertEqual(got, expected)


class TestClosestToZeroFourValues(unittest.TestCase):
    def test_closest_5_9_2_11(self):
        got = closest_to_zero_4(5, 9, 2, 11)
        expected = 2
        self.assertEqual(got, expected)

    def test_closest_0_3_minus_2_4(self):
        got = closest_to_zero_4(0, 3, -2, 4)
        expected = 0
        self.assertEqual(got, expected)

    def test_closest_2_2_minus_2_1(self):
        got = closest_to_zero_4(2, 2, -2, 1)
        expected = 1
        self.assertEqual(got, expected)


class TestClosestToZeroTenValues(unittest.TestCase):
    def test_closest_1_2_3_4_5_6_7_8_9_10(self):
        got = closest_to_zero_10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected = 1
        self.assertEqual(got, expected)

    def test_closest_1_2_minus_1_4_5_0_7_8_9__minus_10(self):
        got = closest_to_zero_10(1, 2, -1, 4, 5, 0, 7, 8, 9, -10)
        expected = 0
        self.assertEqual(got, expected)


class TestClosestToZeroArray(unittest.TestCase):
    def test_closest_5_9(self):
        got = closest_to_zero_all([5, 9])
        expected = 5
        self.assertEqual(got, expected)

    def test_closest_3_minus_2(self):
        got = closest_to_zero_all([3, -2])
        expected = -2
        self.assertEqual(got, expected)

    def test_closest_5_9_2_11(self):
        got = closest_to_zero_all([5, 9, 2, 11])
        expected = 2
        self.assertEqual(got, expected)

    def test_closest_0_3_minus_2_4(self):
        got = closest_to_zero_all([0, 3, -2, 4])
        expected = 0
        self.assertEqual(got, expected)

    def test_closest_1_2_3_4_5_6_7_8_9_10(self):
        got = closest_to_zero_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected = 1
        self.assertEqual(got, expected)

    def test_closest_1_2_minus_1_4_5_0_7_8_9__minus_10(self):
        got = closest_to_zero_all([1, 2, -1, 4, 5, 0, 7, 8, 9, -10])
        expected = 0
        self.assertEqual(got, expected)


class TestStringWithNumbers(unittest.TestCase):
    def test_string_with_1(self):
        got = string_with_numbers(1)
        expected = '1'
        self.assertEqual(got, expected)

    def test_string_with_3(self):
        got = string_with_numbers(3)
        expected = '1_2_3'
        self.assertEqual(got, expected)

    def test_string_with_5(self):
        got = string_with_numbers(5)
        expected = '1_2_3_4_5'
        self.assertEqual(got, expected)

    def test_string_with_0(self):
        got = string_with_numbers(0)
        expected = ''
        self.assertEqual(got, expected)

    def test_string_with_minus_1(self):
        got = string_with_numbers(-1)
        expected = ''
        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main()
