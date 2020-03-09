#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:38:12 2019

@author: sage
"""

from Key_Set import Key_Set
import copy
import random


class Population():
    
    def __init__(self, n_indv, new_rand):
        
        self.n_indv = n_indv
        self.new_rand = new_rand
        self.individuals = [Key_Set() for i in range(self.n_indv)]
        
    def Evaluate(self):
        count = 0 
        for indv in self.individuals:
            indv.Evaluate()
            count+=1
            
            #with open('test', 'a') as f:
            #    f.write(str(count))
            #    f.write('\n')

    def Evaluate_New(self):
        
        for indv in self.individuals:
            if indv.score == None:
                indv.Evaluate()

    def Evaluate_Old(self):
        
        for indv in self.individuals:
            if indv.score != None:
                indv.Evaluate()

    def Tournament(self):
        
        while len(self.individuals) > self.n_indv // 2:
            self.attempt_remove()
            
    def Fill(self):
        
        while len(self.individuals) + self.new_rand < self.n_indv:
            self.add_mutated()
            
        for i in range(self.new_rand):
            self.individuals.append(Key_Set())
            
    def Get_Best_Score(self):
        
        scores = [indv.score for indv in self.individuals if indv.score != None]
        return max(scores)
            
    def attempt_remove(self):
        
        r1, r2 = random.sample(range(len(self.individuals)), 2)
        indv1, indv2 = self.individuals[r1], self.individuals[r2]
        
        if indv1.Compare(indv2):
            del self.individuals[r2]
        elif indv2.Compare(indv1):
            del self.individuals[r1]
            
    def add_mutated(self):
       
        r = random.randint(0, (self.n_indv // 2)-1)
        new_copy = copy.deepcopy(self.individuals[r])
       
        new_copy.Mutate()
        self.individuals.append(new_copy)
            
            
        
    
        
    
