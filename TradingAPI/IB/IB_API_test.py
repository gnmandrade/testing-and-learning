#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:18:53 2022

The current files intends to implement a test of several basic
operations using the IB Trader API for Python.

Objective functions:
    - Get current Portfolio information
    - Get ticker informations (price, volume, bids and asks)
    - Buy/sell limit orders

The current implementation is based on the trial version of
the Interactive Brokers tool, tradding with imaginary funds
to test the tool.


In the initial part of this sample code, the code from the
following tutorial was used:
https://www.youtube.com/watch?v=XKbk8SY9LD0

@author: gnmandrade
"""


# Importing the IB API package
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper


# Variables

#############
# Connect to the platform
#############
# Must be logged in the TWS platform.

# TODO: Note: The tutorial is probably lacking the
#               closing of the connection. Check this topic.

# Class for Interactive Brokers connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
# Bot Logic

class Bot():
    ib = None
    def __init__(self):
        # Build connection on init
        ib = IBApi()
        ib.connect('127.0.0.1',7497,1)
        ib.run()
        
# Start Bot
bot = Bot()
