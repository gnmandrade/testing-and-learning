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
TODO: Currently implementing this second tutorial
https://www.youtube.com/watch?v=tWwHNP1Yh1g

Details on the TWS API contracts for getting information:
https://interactivebrokers.github.io/tws-api/basic_contracts.html

@author: gnmandrade
"""


# Importing the IB API package
import ibapi
# These imports are for the initial connection
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

# For data streaming
from ibapi.contract import Contract

# To submit orders
from ibapi.order import *

# To host the data streaming in a different thread
import threading

# To deal with time data
import time

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
        
    # Method to listen for realtime bars
    def realtimeBar(self, reqID, time, open_, high, low, close, volume, wap, count):
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e:
            print(e)
        
    def error(self, id, errorCode, errorMsg):
        print(errorCode)
        print(errorMsg)
        
# Bot Logic

class Bot():
    ib = None
    def __init__(self):
        # Build connection on init
        self.ib = IBApi()
        self.ib.connect('127.0.0.1',7497,1)
        # The run needs to be sent to a different thread
        # Check run_loop method
        #ib.run()
        ib_thread = threading.Thread(target=self.run_loop, deamon=True)
        ib_thread.start()
        
        # Sleep to avoid being interrupted by the connect
        # messages
        time.sleep(3)
        
        # Input symbol to trade
        symbol = input("Enter the symbol you want to trade: ")
        
        # Create Contract object
        # These are the objects IB uses to stream data
        # or submit orders
        contract = Contract()
        
        # Set the symbol
        contract.symbol = symbol.upper()
        # Define type of symbol
        # In this case it is a stock
        contract.secType = 'STK'
        
        # Define the exchange
        # SMART is an automatic selection, but we can force
        # a given exchange to be used
        contract.exchange = 'SMART'
        
        # Define currency
        contract.currency = 'USD'
        
        # Request Market data
        # The first argument is the request ID, which
        # should start with 0 and increase over time as
        # our application runs
        # Second arg is our contract object
        # Third arg has a minimum size of 5
        #
        # More info for this method available in:
        # https://interactivebrokers.github.io/tws-api/classIBApi_1_1EClient.html#a644a8d918f3108a3817e8672b9782e67
        self.ib.reqRealTimeBars(0, contract, 5, 'TRADES', 1, [])
    # Put the run in a different thread
    def run_loop(self):
        self.ib.run()
    
    # Pass realtime bar data back to our bot object
    def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
        print(reqId)
    
# Start Bot
bot = Bot()
