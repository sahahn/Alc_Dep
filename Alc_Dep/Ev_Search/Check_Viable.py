# -*- coding: utf-8 -*-

from Population import Population
import os
import pickle

def check_pop(file, thresh):
    with open(file, 'rb') as f:
        pop = pickle.load(f)
        
    viable = []
    
    for indv in pop.individuals:
        if indv.score != None:
            if indv.score > thresh:
                viable.append(indv.keys)
                
        
    return viable

def get_best(file):
    with open(file, 'rb') as f:
        pop = pickle.load(f)

    best = pop.Get_Best_Score()
    return best
