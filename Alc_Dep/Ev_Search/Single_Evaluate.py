# -*- coding: utf-8 -*-

"""
Created on Wed Jan  9 11:39:34 2019

@author: sage
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from keys import keys as all_keys
from config import config
import argparse

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

parser = argparse.ArgumentParser()
parser.add_argument('--keys', nargs='+', type=int)
args = parser.parse_args()

params = {"C": np.linspace(1, 100000, 500),
          "tol": np.linspace(.000001, 1, 1000),
  	      "gamma": np.linspace(.000001, 1, 500)}

def load_data(loc, drop_keys=None, inclusion_keys=None):
    '''Function to load the dataset given a location, and optional drop and inclusion keys'''
    
    #Csv specific stuff~~~
    data = pd.read_csv(loc, na_values=['#NULL!', ''])
    data = data.drop(['PI', 'Subject', 'Dependent = 1', 'Unnamed: 4', 'Unnamed: 19',
     'Unnamed: 20', 'Unnamed: 89'], axis=1)
    #data = data.dropna(axis='rows', how='any', thresh=145)
    #data = data.fillna(data.mean())
    data = data.dropna(axis='columns', how='all')
    data = data.dropna()

    if drop_keys != None:
        
        to_remove = set()
        col_names = list(data)

        for name in col_names:
            for key in drop_keys:
                if key in name:
                    to_remove.add(name)

        data = data.drop(list(to_remove), axis=1)
        
    if inclusion_keys != None:
        
        inclusion_keys.append('Dependent')
        
        to_remove = set()
        col_names = list(data)
        
        for name in col_names:
            flag = False
            
            for key in inclusion_keys:
                if key in name:
                    flag = True
            
            if not flag:
                to_remove.add(name)
                
        data = data.drop(list(to_remove), axis=1)
            
    
    X = np.array(data.drop('Dependent', axis=1))
    y = np.array(data.loc[:, 'Dependent'])
    
    return X,y
    
def do_random_search(clf, params, skf, X_train, y_train, X_test, y_test):
    '''Helper function to preform a random search over different params'''
    
    rs = RandomizedSearchCV(clf, param_distributions=params,
                           n_iter=100,
                           scoring='roc_auc',
                           n_jobs=-1,
                           cv=skf.split(X_train,y_train))
    
    rs.fit(X_train, y_train)

    scores = rs.predict_proba(X_test)
    scores = [s[1] for s in scores]
    auc = roc_auc_score(y_test, scores)

    #For case where it returns the class scores flipped
    if auc < .5:
        scores = rs.predict_proba(X_test)
        scores = [s[0] for s in scores]
        auc = roc_auc_score(y_test, scores)

    return auc

def Run_Evaluation_Old(keys):
    '''Evaluation method called by a Key_Set'''
    
    keys = [all_keys[a] for a in keys]
   
    if not config['all']:
        keys = [key + '_thickavg' for key in keys]
    

def Run_Evaluation(keys):
    '''Evaluation method called by a Key_Set'''

    e,g,h = loaders.load_it_all(age=False, sex=False, split_enigma=False)
    X,y	= e

    X = X[:,keys]

    m, st = ML.run_binary_search(X, y, n_splits=3, n_repeats=20, int_folds=3, param_comb=100)
    return m




keys = args.keys

score = Run_Evaluation(keys)
key_names = sorted([all_keys[i] for i in keys])

print(score, key_names)

