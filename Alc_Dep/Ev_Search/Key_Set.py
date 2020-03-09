#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:25:41 2019

@author: sage
"""

from keys import keys
from config import config
from Evaluate import Run_Evaluation
import random

class Key_Set():
    
    def __init__(self):
        
        self.n_options = len(keys)
        self.score = None

        start_num = config['start_num'] + random.randint(0,2)
        self.keys = random.sample(range(self.n_options), start_num)
        
    def Evaluate(self):
        
        self.score = Run_Evaluation(self.keys)
        
        
    def Compare(self, other):

        if set(self.keys) == set(other.keys):
            return True
        
        if self.score > other.score and len(self.keys) <= len(other.keys):
            return True
        
        return False
        
        
    def Mutate(self):
        
        r = random.random()
        
        if r < config['change_chance']:
            self.change_key()
        else:
            if len(self.keys) > config['start_num']:
                r = random.random()
                
                if r < config['change_chance']:
                    self.remove_key()
                else:
                    self.add_key()
            else:
                self.add_key()

        self.score = None
            
    def change_key(self):
        
        to_change = random.randint(0, len(self.keys)-1)
        new = random.randint(0, self.n_options-1)
        
        while new in self.keys:
            new = random.randint(0, self.n_options-1)
            
        self.keys[to_change] = new
        
    def add_key(self):
        
        new = random.randint(0, self.n_options-1)
        
        while new in self.keys:
            new = random.randint(0, self.n_options-1)
            
        self.keys.append(new)

    def remove_key(self):
        
        to_del = random.randint(0, len(self.keys)-1) 
        del self.keys[to_del]      
  
    def get_key_names(self):
        
        return sorted([keys[i] for i in self.keys])
        
        
            
        
        
        
        
        
        
        
        
        
        
