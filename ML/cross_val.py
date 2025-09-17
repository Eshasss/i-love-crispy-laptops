import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import r2_score

def kfold_split(X, y,  n):
    X_folds = []
    y_folds = []

    r = X.shape[0]
    row_l = r//n
    for i in range(0, r, row_l):
        X_folds.append((X[i:i+row_l], np.concatenate((X[0:i],X[i+row_l:]), axis=0)))
        y_folds.append((y[i:i+row_l], np.concatenate((y[0:i],y[i+row_l:]), axis=0)))
    return X_folds, y_folds

def knn_cv_score(X, y,n, n_n, metric, weight, scorer, norm, model=KNeighborsRegressor):
    X_folds, y_folds = kfold_split(X, y, n)
    y_tests = []
    y_preds =[]
    for i in range(n):
        X_test = X_folds[i][0]
        X_train = X_folds[i][1]
        y_test = y_folds[i][0]
        y_train = y_folds[i][1]
        if norm is not None:
                X_train_scaled = norm.fit_transform(X_train).toarray()
                X_test_scaled = norm.transform(X_test).toarray()
        else:
                X_train_scaled = X_train
                X_test_scaled = X_test
        neigh = model(n_neighbors=n_n, metric=metric, weights=weight)
        neigh.fit(X_train_scaled, y_train)
        y_pred = neigh.predict(X_test_scaled)
        # y_preds.append(y_pred)
        # y_tests.append(y_test)
        y_preds.extend(y_pred.tolist())
        y_tests.extend(y_test.tolist())
    return scorer(y_tests, y_preds)

def knn_cv_score_ignore(X, y, n, n_n, metric, weight, random_state=None ):
    # работающий костыльчик
    scores = 0
    preds = []
    X_mod, y_mod = np.split(X, n, axis=0), np.split(y, n, axis=0)

    for i in range(n):
        X_test = X_mod[i]
        y_test = y_mod[i]
        X_train = np.delete(X_mod, i, axis=0).reshape(-1,  X.shape[-1])
        y_train = np.delete(y_mod, i, axis=0).reshape(-1)
        neigh = KNeighborsRegressor(n_neighbors=n_n, metric=metric, weights=weight)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_test)
        preds.append((y_test, y_pred))
        scores += r2_score(y_test, y_pred)
    return scores/n
