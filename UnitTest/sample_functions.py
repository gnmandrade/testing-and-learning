#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:51:30 2022

Sample functions and classes to learn unitTest

@author: gnmandrade
"""

def add_function(a, b):
    return a + b

def cast_to_str(a):
    return int(a)

def compute_result(list_n):
    result = 0
    for x in list_n:
        result += x
    
    return result

def has_same_type(a, b):
    return type(a) == type(b)
