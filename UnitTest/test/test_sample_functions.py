#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:50:51 2022

File to test UnitTest

@author: gnmandrade
"""

import unittest
import sample_functions as sFuncs

class TestSampleFunctions(unittest.TestCase):
    test_list1 = [1,2,3,4]
    test_list2 = [6,8,3.0,4.33]
    test_list3 = [1,2,3,'4']
    test_list4 = [1,2,3,'a']
    test_list5 = ['1','2','3','a']
    
    def test_add_function(self):
        self.assertEqual(sFuncs.add_function(2, 3), 5)
        self.assertEqual(sFuncs.add_function(5, 5), 10)
        self.assertEqual(sFuncs.add_function(1, 14), 15)
        self.assertEqual(sFuncs.add_function(0.3, 3), 3.3)
        self.assertEqual(sFuncs.add_function(0, 10), 10)
        
    def test_has_same_type(self):
        self.assertTrue(sFuncs.has_same_type('3','a'))
        self.assertFalse(sFuncs.has_same_type(2, 2.0))
        
    def test_compute_result(self):
        self.assertEqual(sFuncs.compute_result(self.test_list1), 10)
                
        with self.assertRaises(Exception):
            sFuncs.compute_result(self.list3)
            
        with self.assertRaises(Exception):
            sFuncs.compute_result(self.list4)
        
        with self.assertRaises(Exception):
            sFuncs.compute_result(self.list5)
    
        
        
if __name__ == '__main__':
    unittest.main()