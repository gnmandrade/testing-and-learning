#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:00:15 2022

Learning parallel computing in Python.

File based on the tutorial available in:
https://www.machinelearningplus.com/python/parallel-processing-python/

@author: gnmandrade
"""

# Import usual libraries
import numpy as np
import pandas as pd

from time import time

# Import multiprocessing library
import multiprocessing as mp


# Find out number of processors
print("Number of processors: ", mp.cpu_count())


# Count number of elements in a given range

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size = [200000, 5])
data = arr.tolist()

# Print first 5 elements
print(data[:5])








