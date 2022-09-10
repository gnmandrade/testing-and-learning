#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:22:10 2022

File for customized process class

@author: gnmandrade
"""

import time
import multiprocessing as mp

def countdown(name, delay, count):
    while count:
        time.sleep(delay)
        print(f'{name, time.ctime(time.time()), count}')
        count -= 1
    
# Inheriting the mp.Process class into newProcess
class newProcess(mp.Process):
    # Overriding the __init__ method
    def __init__(self, name, count):
        # First we execute the regular __init__ method
        # from mp.Process
        mp.Process.__init__(self)
        # After we apply our changes
        self.name = name
        self.count = count
        
    # Overriding the run() method
    def run(self):
        print("Starting: " + self.name + "\n")
        countdown(self.name, 1, self.count)
        print("Exiting: " + self.name + "\n")
        