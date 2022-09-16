#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:40:02 2022

Based on the tutorial:
https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7009489-implement-the-controller-and-view-for-your-application

@author: gnmandrade
"""

class InternetStreamingView:
    def show_player_and_hand(self, player_name, hand):
        # The code for broadcasting should go here
        pass
    
    def show_winner(self, winner_name):
        # Full implementation should go in here
        pass
    
    
class BroadcastView:
    def show_player_and_hand(self, player_name, hand):
        # The code for broadcasting should go here
        pass
    
    def show_winner(self, winner_name):
        # Full implementation should go in here
        pass
    
    
class PlayerView:
    def prompt_for_new_player(self):
        new_player = input("Type name of player: ")
        if new_player =="":
            return None
        return new_player
    
    def show_player_and_hand(self, player_name, hand):
        print('[' + player_name + ']')
        for card in hand.cards:
            if card.face_up:
                print(card.name())
            else:
                print("(hidden card)")
                
    def prompt_for_flip_cards(self):
        print("")
        prompt = input("Ready to see who won?")
        return True
    
    def show_winner(self, winner_name):
        print("")
        print("Congratulations " + winner_name + "!!!")
        
    def prompt_for_new_game(self):
        print("")
        while True:
            prompt = input("Play again? Y/N: ")
            if prompt == 'Y':
                return True
            if prompt == 'N':
                return False