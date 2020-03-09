"""
Created on Wed Jan  9 11:39:34 2019

@author: sage
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedKFold, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from keys import keys as all_keys
from config import config
import loaders
import ML

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def Run_Evaluation(keys):
    keys = [all_keys[a] for a in keys]

    (X,y), (X_test, y_test), qq, qqq = loaders.load_it_all(split_enigma=True, i_keys=keys)

    scores = []
    for q in range(config['n_repeats']):
        model = ML.train_model(X, y, param_comb=config['num_searches'], classifier='log')
        scores.append(ML.get_roc(model, X_test, y_test))

    return np.mean(scores)

