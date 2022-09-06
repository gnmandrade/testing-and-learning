#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:00:15 2022

Learning parallel computing in Python.

File based on the tutorial available in:
https://www.machinelearningplus.com/python/parallel-processing-python/

@author: gnmandrade
"""

if __name__ == '__main__':
    
    # Import usual libraries
    import numpy as np
    import pandas as pd
    
    from time import time
    
    # Import multiprocessing library
    import multiprocessing as mp
    
    
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
    
    
    #######
    # Compute without parallelization
    #######
    
    def howmany_between_range(row, minimum, maximum):
        # Returns the number of numbers between minimum and maximum
        count = 0
        
        for n in row:
            if minimum <= n <= maximum:
                count = count + 1
                
        return count
    
    # Declare result list
    results = []
    
    minimum = 4
    maximum = 8
    
    for row in data:
        results.append(howmany_between_range(row, minimum, maximum))
    
    # Print first 10 results
    print(results[:10])
    
    #######
    # Parallelize with pool.apply()
    #######
    
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())
    
    # Step 2: 'pool.apply' the 'howmany_between_range' function
    results2 = [pool.apply(howmany_between_range, args = (row, 4, 8)) for row in data]
    
    # Step 3: Close the pool
    pool.close()
    
    
    print(results2[:10])