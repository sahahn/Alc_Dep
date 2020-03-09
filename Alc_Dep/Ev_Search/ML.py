import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import SGDClassifier
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def get_roc(model, X, y):

    scores = model.predict_proba(X)
    scores = [s[1] for s in scores]

    auc = roc_auc_score(y, scores)

    return auc

def do_random_search(clf, params, skf, X_train, y_train, X_test, y_test, param_comb):
    
    rs = RandomizedSearchCV(clf, param_distributions=params,
                           n_iter=param_comb,
                           scoring='roc_auc',
                           n_jobs=-1,
                           cv=skf.split(X_train,y_train))
    
    rs.fit(X_train, y_train)
    score = get_roc(rs, X_test, y_test)
        
    return score


def run_binary_search(X, y, classifier='SVM', n_splits=3, n_repeats=50, int_folds=3, param_comb=100, verbose=False):

    skf = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats)

    if classifier == 'SVM':
        params = {"C": np.linspace(1, 100000, 500),
                  "tol": np.linspace(.000001, 1, 1000),
                  "gamma": np.linspace(.000001, 1, 500)}

    elif classifier == 'RF':
        params = {"n_estimators": list(range(3,400)),
                  "max_depth": [None] + list(range(2,80)),
                  "max_features": list(range(1,68)),
                  "min_samples_split": list(range(2,83)),
                  "bootstrap": [True],
                  "criterion": ["gini"]}

    elif classifier == 'SGD':
        params = {"loss": ['modified_huber', 'log'],
                  "penalty": ['elasticnet'],
                  "l1_ratio" : np.linspace(.000001, 1, 1000),
                  "alpha" : np.linspace(.000001, 1, 1000)
                  }

    scores = []

    count = 0
    for train_ind, test_ind in skf.split(X,y):
        
        X_train, y_train = X[train_ind], y[train_ind]
        X_test, y_test = X[test_ind], y[test_ind]

        skf = StratifiedKFold(n_splits=int_folds, shuffle = True)
            
        if classifier == 'SVM':
            clf = SVC(probability=True, class_weight='balanced')
            score = do_random_search(clf, params, skf, X_train, y_train, X_test, y_test, param_comb)
        
        elif classifier == 'RF':
            clf = RandomForestClassifier()
            score = do_random_search(clf, params, skf, X_train, y_train, X_test, y_test, param_comb)

        elif classifier == 'SGD':
            clf = SGDClassifier(max_iter=10000, tol=1e-3)
            score = do_random_search(clf, params, skf, X_train, y_train, X_test, y_test, param_comb)
        
        elif classifier == 'log':
            clf = LogisticRegressionCV(cv=int_folds, class_weight='balanced')
            
            clf.fit(X_train, y_train)
            score = get_roc(clf, X_test, y_test)

        scores.append(score)
            
        if verbose:
            print('score = ', score)

        count += 1

        if (count % n_splits == 0) and verbose:
            print(count//n_splits, '/', n_repeats) 

    if verbose:
        print(classifier)

    return np.mean(scores), np.std(scores)
            

def train_model(X, y, int_folds=3, param_comb=100, classifier='SVM'):

    skf = StratifiedKFold(n_splits=int_folds, shuffle = True)

    if classifier == 'SVM':
        params = {"C": np.linspace(1, 100000, 500),
                "tol": np.linspace(.000001, 1, 1000),
                "gamma": np.linspace(.000001, 1, 500)}

        clf = SVC(probability=True, class_weight='balanced')

    elif classifier == 'RF':
        params = {"n_estimators": list(range(3,400)),
                "max_depth": [None] + list(range(2,80)),
                "max_features": list(range(1,68)),
                "min_samples_split": list(range(2,83)),
                "bootstrap": [True],
                "criterion": ["gini"]}

        clf = RandomForestClassifier()

    elif classifier == 'SGD':
        params = {"loss": ['modified_huber', 'log'],
                  "penalty": ['elasticnet'],
                  "l1_ratio" : np.linspace(.000001, 1, 1000),
                  "alpha" : np.linspace(.000001, 1, 1000)
                  }

        clf = SGDClassifier(max_iter=10000, tol=1e-3)

    elif classifier == 'log':

        clf = LogisticRegressionCV(cv=int_folds, class_weight='balanced')
        clf.fit(X, y)

        return clf


    rs = RandomizedSearchCV(clf, param_distributions=params,
                           n_iter=param_comb,
                           scoring='roc_auc',
                           n_jobs=-1,
                           cv=skf.split(X,y))
    
    rs.fit(X, y)

    return rs






