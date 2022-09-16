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
# Deck
deck = Model.Deck()

# Create Views
player_view = View.PlayerView()
view_1 = View.BroadcastView()
view_2 = View.InternetStreamingView()


gameEvaluator = Controler.HighCardGameEvaluator()

# Create game controler
gameControler = Controler.Controler(deck, player_view, view_1, view_2, gameEvaluator )
gameControler.run()