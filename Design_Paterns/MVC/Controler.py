#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:39:28 2022

Based on the tutorial:
https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7009489-implement-the-controller-and-view-for-your-application

@author: gnmandrade
"""

import Model

class Controler:
    def __init__(self, deck, view):
        # Model
        self.players = []
        self.deck = deck
        
        # View
        self.view = view
        
    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)
    
    def evaluate_game(self):
        best_candidate = None
        
        for player in self.players:
            if best_candidate is None:
                best_candidate = player
                continue
            
            if player.hand.card_by_index(0).is_better_than(
                    best_candidate.hand.card_by_index(0)):
                best_candidate = player
                
        return best_candidate.name
             
    def rebuild_deck(self):
        for player in self.players:
            while player.hand.cards:
                this_card = player.hand.remove_card()
                this_card.face_up = False
                self.deck.add_card(this_card)
        self.deck.shuffle()
    
    def add_player(self, player_name):
        self.players.append(Model.Player(player_name))
    
    def run(self):
        while len(self.players) < 5:
            new_player = self.view.prompt_for_new_player()
            if new_player is None:
                break
            self.add_player(new_player)
        
        while True:
            self.start_game()
            
            for player in self.players:
                self.view.show_player_and_hand(player.name, player.hand)
                
            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True
                self.view.show_player_and_hand(player.name, player.hand)
                
            self.view.show_winner(self.evaluate_game())
            
            if not self.view.prompt_for_new_game():
                break
            
            self.rebuild_deck()