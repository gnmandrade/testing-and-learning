#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:38:12 2022

Tests for the sample class.

@author: gnmandrade
"""

import unittest
import sample_class

class TestSampleClass(unittest.TestCase):
    def setUp(self):
        self.table1 = sample_class.TableClass(3)
        
    def test_add_all(self):
        self.assertEqual(self.table1.add_all(), 9)
        
    def test_sample_class_type(self):
        self.assertTrue(isinstance(self.table1,sample_class.TableClass))
        
        
if __name__ == '__main__':
    unittest.main()