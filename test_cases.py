#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #有効同値でのテスト
        def test_Valid_values01(self):
                self.assertEqual(250000, calc(500, 500))

        def test_Valid_values02(self):
                self.assertEqual(180000,calc(300, 600))

        def test_Valid_values03(self):
                self.assertEqual(180000, calc(600, 300))
        
        #境界値付近でのテスト
        def test_boundary_values01(self):
                self.assertEqual(1, calc(1, 1))
        
        def test_boundary_values02(self):
                self.assertEqual(-1, calc(0, 1))
        
        def test_boundary_values03(self):
                self.assertEqual(-1, calc(0, 0))

        def test_boundary_values04(self):
                self.assertEqual(999, calc(999, 1))
        
        def test_boundary_values05(self):
                self.assertEqual(-1, calc(1000, 1))
        
        def test_boundary_values06(self):
                self.assertEqual(999, calc(1, 999))

        def test_boundary_values07(self):
                self.assertEqual(-1, calc(-1, 999))

        def test_boundary_values08(self):
                self.assertEqual(998001, calc(999, 999))
        
        def test_boundary_values09(self):
                self.assertEqual(-1, calc(1000, 999))
        
        def test_boundary_values10(self):
                self.assertEqual(-1, calc(999, 1000))
        
        def test_boundary_values11(self):
                self.assertEqual(-1, calc(1000, 1000))
        
        #無効同値でのテスト
        def test_Fail_values01(self):
                self.assertEqual(-1, calc(-100, 999))
        
        def test_Fail_values02(self):
                self.assertEqual(-1, calc(5000, 4000))

        #その他(記号、小数点など)
        def test_other_values01(self):
                self.assertEqual(-1, calc(None, 600))
        
        def test_other_values02(self):
                self.assertEqual(-1, calc(500, None))

        def test_other_values03(self):
                self.assertEqual(-1, calc('Z', 999))
        
        def test_other_values04(self):
                self.assertEqual(-1, calc(999, 'A'))
        
        def test_other_values05(self):
                self.assertEqual(-1, calc(0.1, 500))
        
        def test_other_values06(self):
                self.assertEqual(-1, calc(500, 0.1))