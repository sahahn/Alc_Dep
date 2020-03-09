# -*- coding: utf-8 -*-
config = {}

#GENERAL EV. SEARCH CONFIGS
#-------------------------

#Number of Key_Set individuals to have in the population
config['n_indv'] = 100

#Number of generations to evaluate over
config['num_gens'] = 50

#Number of new random Key_Sets to add in each Fill
config['new_rand'] = 3

#Number of keys to start with on a new random Key Set
config['start_num'] = 3

#Prob. for mutate to change a key vs. add a new key
config['change_chance'] = .8

#If True, keys are refined to Left and Right seperate, otherwise not
config['LR_specific'] = True

config['all'] = True

#SETTINGS FOR EACH RANDOM SEARCH
#-------------------------------

config['loc'] = None

#Number of CV splits to evaluate
config['n_splits'] = 3

#Number of times to repeat CV search
config['n_repeats'] = 1

#Number of random params to search during each fold
config['num_searches'] = 100

#Number of jobs to use during evaluation
config['n_jobs'] = -1

