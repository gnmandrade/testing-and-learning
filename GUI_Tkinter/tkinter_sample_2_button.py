#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:12:28 2022

Sample code for a GUI based on the following tutorial:
https://www.tutorialspoint.com/python/tk_button.htm

@author: gnmandrade
"""

# Import the library used to build the GUI
import tkinter as tk

# Create the frame object
top = tk.Tk()

# Define function to answer when button is pressed
def helloCallBack():
    M = tk.Message(top, text = 'Success!!!')
    M.pack()

# Create button    
B = tk.Button(top, text = 'Greetings', command = helloCallBack)

# Pack the button
B.pack()

# Code with the objects should be here and before the main loop

# Main loop that shows the window
top.mainloop()