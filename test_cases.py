#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 正常系
        def test_valid_case1(self):
                self.assertEqual(calc(1, 1), 1)

        def test_valid_case2(self):
                self.assertEqual(calc(10, 20), 200)

        def test_valid_case3(self):
                self.assertEqual(calc(999, 999), 998001)

        # 範囲外（小）
        def test_out_of_range_low1(self):
                self.assertEqual(calc(0, 500), -1)

        def test_out_of_range_low2(self):
                self.assertEqual(calc(-10, 500), -1)

        # 範囲外（大）
        def test_out_of_range_high1(self):
                self.assertEqual(calc(1000, 500), -1)

        def test_out_of_range_high2(self):
                self.assertEqual(calc(500, 1000), -1)

        # 型不正（小数）
        def test_invalid_type_float1(self):
                self.assertEqual(calc(1.5, 100), -1)

        def test_invalid_type_float2(self):
                self.assertEqual(calc(100, 2.3), -1)

        # 型不正（文字列）
        def test_invalid_type_str1(self):
                self.assertEqual(calc("100", 5), -1)

        def test_invalid_type_str2(self):
                self.assertEqual(calc(5, "100"), -1)

        # 型不正（リスト）
        def test_invalid_type_list(self):
                self.assertEqual(calc([10, 20], 5), -1)

        # 型不正（None）
        def test_invalid_type_none(self):
                self.assertEqual(calc(None, 10), -1)