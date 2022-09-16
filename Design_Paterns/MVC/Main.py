#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:04:07 2022

Code to run the MVC application

@author: goncalo
"""

import Model
import Controler
import View

# Create inputs for the controler
# Deck and View
deck = Model.Deck()
view = View.View()

gameEvaluator = Controler.HighCardGameEvaluator()

# Create game controler
gameControler = Controler.Controler(deck, view, gameEvaluator )
gameControler.run()