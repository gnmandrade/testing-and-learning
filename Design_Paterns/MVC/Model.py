#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:41:01 2022

Following the tutorial on:
https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7009396-implement-the-model-for-your-application

@author: gnmandrade
"""

import random

SUITS = {
    "Diamonds": 1,
    "Hearts": 2,
    "Spades": 3,
    "Clubs": 4        
}

RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eigth": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14    
}


class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False
        
    def name(self):
        return " ".join([self.rank, "of", self.suit])
    
    def is_better_than(self, other_card):
        other_rank = RANKS[other_card.rank]
        our_rank = RANKS[self.rank]
        
        if our_rank > other_rank:
            return True
        if our_rank < other_rank:
            return False
        
        other_suit = SUITS[other_card.suit]
        our_suit = SUITS[self.suit]
        
        return (our_suit > other_suit)
    

class Deck:
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(PlayingCard(suit, rank))
        self.shuffle()
        
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def remove_top_card(self):
        return self.cards.pop()
    
    
class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def card_by_index(self, index):
        try:
            return self.cards[index]
        except Exception:
            return None
        
    def remove_card(self):
        if not self.cards:
            return None
        return self.cards.pop()
    
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()