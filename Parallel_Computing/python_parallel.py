#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:00:15 2022

Learning parallel computing in Python.

File based on the tutorial available in:
https://www.machinelearningplus.com/python/parallel-processing-python/

As the first tutorial was getting stuck, we tried the
following one:
https://analyticsindiamag.com/run-python-code-in-parallel-using-multiprocessing/

@author: gnmandrade
"""

# Import usual libraries
import numpy as np
import pandas as pd
import sys

import time as tm
from time import time

# Import Helper library
wdir = '/home/goncalo/Documents/python_projects/0-learning/testing-and-learning/Parallel_Computing/'

try:
    test = sys.path.index(wdir)
except:
    sys.path.append(wdir)

# Import parallelization methods
import parallelization_methods as p_methods
import my_process

# Import multiprocessing library
import multiprocessing as mp


# Workaround for the multiprocessing to work
#sys.modules['__main__'].__file__ = 'ipython'

# Find out number of processors
print("Number of processors: ", mp.cpu_count())


# Count number of elements in a given range

#######
# Prepare data
#######

np.random.RandomState(100)
arr = np.random.randint(0, 10, size = [200000, 5])
data = arr.tolist()

# Print first 5 elements
print(data[:5])


# Function to parallelize
def howmany_between_range(row, minimum, maximum):
    # Returns the number of numbers between minimum and maximum
    count = 0
    
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
            
    return count


#######
# Compute without parallelization
#######

results = p_methods.no_parallelization(data, howmany_between_range)

# Print first 10 results
print(results[:10])

#######
# Parallelize with pool.apply()
#######
# This code does not stop
# Review this part
#results2 = p_methods.parallelize_w_pool_apply(data, howmany_between_range)

#print(results2[:10])


###
# Trying second tutorial
###

# First code
def test_function(sec = 1):
    print(f'Sleeping for {sec} seconds(s)...')
    tm.sleep(sec)
    print("Done sleeping!")

start = tm.perf_counter()
# Declaring the processes
process1 = mp.Process(target = test_function)
process2 = mp.Process(target = test_function)

# Starting processes
process1.start()
process2.start()

# Telling the interpreter for wait for the processes to end
process1.join()
process2.join()

end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")

######
# Test several processes
######

start = tm.perf_counter()
# Declaring the processes
processes = []

# The item in the args list is the argument of the function
for _ in range(10):
    p = mp.Process(target=test_function, args = [2])
    # Starting processes
    p.start()
    processes.append(p)

# Telling the interpreter for wait for the processes to end
# This needs to be done in a separate loop,
# otherwise the interpreter will wait for each
# process to finish
for p in processes:
    p.join()

end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")



###########
# Create a class for custom process
###########

