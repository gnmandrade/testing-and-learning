#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:55:29 2022

Auxiliar file to contain functions with the different
parallelization methods

@author: gnmandrade
"""

# Import multiprocessing library
import multiprocessing as mp

#######
# Compute without parallelization
#######

def no_parallelization(data, func_to_use):
    # Declare result list
    results = []
    
    minimum = 4
    maximum = 8
    
    for row in data:
        results.append(func_to_use(row, minimum, maximum))

    return results


#######
# Parallelize with pool.apply()
#######

def parallelize_w_pool_apply(data, func_to_use):
    
    print(__name__)
    if __name__ == 'parallelization_methods':
        minimum = 4
        maximum = 8
        
        # Step 1: Init multiprocessing.Pool()
        #pool = mp.Pool(mp.cpu_count())
        with mp.get_context("spawn").Pool() as pool:
        
            # Step 2: 'pool.apply' the 'howmany_between_range' function
            results = [pool.apply(func_to_use, args = (row, 4, 8)) for row in data]
            
            # Step 3: Close the pool
            pool.close()
    
        return results
