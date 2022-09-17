#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:37:06 2022

Sample Class to test with unittest

@author: gnmandrade
"""

class TableClass:
    table = None
    size = None
    
    def __init__(self, size):
        self.size = size
        self.table = [[1 for x in range(size)] for y in range(size)]
        print(self.table)
        
    def add_all(self):
        result = 0
        for x in self.table:
            for y in x:
                result += y
                
        return result
