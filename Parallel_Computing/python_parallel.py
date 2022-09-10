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
# Test the created class

t = my_process.newProcess("New Process 1", 5)
t.start()
t.join()

print("Done!!!")



###########
# Parallelize with ProcessPoolExecutor
###########

import concurrent.futures

# With only 2 processes
start = tm.perf_counter()
def useless_function(sec = 1):
    print(f'Sleeping for {sec} seconds(s)...')
    tm.sleep(sec)
    print("Done sleeping!")
    return sec

with concurrent.futures.ProcessPoolExecutor() as executor:
    process1 = executor.submit(useless_function, 1)
    process2 = executor.submit(useless_function, 1)
    
    print(f'Return Value: {process1.result()}')
    print(f'Return Value: {process2.result()}')

end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")

# With only n processes
# use of the as_completed() method
start = tm.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    
    # Create pool of executions
    pool = [executor.submit(useless_function, i) for i in secs]
    
    for i in concurrent.futures.as_completed(pool):
        print(f'Return Value: {i.result()}')
    
end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")


# Using the map method to retrieve the results
start = tm.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    
    # Submit and get results of all processes
    pool = executor.map(useless_function, secs)
    for res in pool:
        print(f'Return Value: {res}')
    
end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")



###########
# Parallelize Image processing with ProcessPoolExecutor
###########

from PIL import Image, ImageFilter

input_folder = wdir + 'sample_images/'
output_folder = wdir + 'output_images/'

file_names = ['pexels-stein-egil-liland-3408744.jpg',
              'pexels-roberto-nickson-2559941.jpg',
              'pexels-luis-del-río-15286.jpg',
              'pexels-kammeran-gonzalezkeola-7925859.jpg',
              'pexels-jaime-reimer-2662116.jpg',
              'pexels-jacob-colvin-1757363.jpg',
              'pexels-frans-van-heerden-624015.jpg',
              'pexels-francesco-ungaro-1671324.jpg',
              'pexels-ezra-comeau-2387418.jpg',
              'pexels-eberhard-grossgasteiger-572897.jpg',
              'pexels-asad-photo-maldives-1591373.jpg']

# Running sequentially
start = tm.perf_counter()
size = (1200,1200)

def augmented_image(img_name, input_folder, output_folder):
    img = Image.open(input_folder + img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'{output_folder}augmented-{img_name}')
    print(f'{img_name} was augmented...')
    
for f in file_names:
    augmented_image(f, input_folder, output_folder)
    
end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")


# Running with ProcessPoolExecutor
start = tm.perf_counter()
size = (1200,1200)

def augmented_image2(img_name, input_folder, output_folder):
    img = Image.open(input_folder + img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'{output_folder}augmented_V2-{img_name}')
    print(f'{img_name} was augmented...')


input_folders = [input_folder for x in file_names]
output_folders = [output_folder for x in file_names]

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(augmented_image2, file_names, input_folders, output_folders)
    
    
end = tm.perf_counter()
print(f"Process run in {round(end - start, 2)} seconds(s).")
