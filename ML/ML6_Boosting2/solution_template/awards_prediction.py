# У меня получился минимальный мае 2090
import pandas as pd
import optuna
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor



from numpy import ndarray

from sklearn.feature_extraction.text import TfidfVectorizer

"""
 Внимание!
 В проверяющей системе имеется проблема с catboost.
 При использовании этой библиотеки, в скрипте с решением необходимо инициализировать метод с использованием `train_dir` как показано тут:
 CatBoostRegressor(train_dir='/tmp/catboost_info')
"""
def tfidf(df_train, df_test, column_name, prefix, max_features=20):
    df_train[f'{column_name}_text'] = df_train[column_name].apply(lambda x: " ".join(x) if isinstance(x, list) else "")
    df_test[f'{column_name}_text'] = df_test[column_name].apply(lambda x: " ".join(x) if isinstance(x, list) else "")

    vectorizer = TfidfVectorizer(max_features=max_features)
    X_train = vectorizer.fit_transform(df_train[f'{column_name}_text'])
    X_test = vectorizer.transform(df_test[f'{column_name}_text'])

    df_train_cols = pd.DataFrame(X_train.toarray(), columns=[f'{prefix}_{i}' for i in range(X_train.shape[1])])
    df_test_cols = pd.DataFrame(X_test.toarray(), columns=[f'{prefix}_{i}' for i in range(X_test.shape[1])])

    df_train = pd.concat([df_train.reset_index(drop=True), df_train_cols], axis=1)
    df_test = pd.concat([df_test.reset_index(drop=True), df_test_cols], axis=1)

    del df_train[column_name]
    del df_train[f'{column_name}_text']
    del df_test[column_name]
    del df_test[f'{column_name}_text']

    return df_train, df_test

def objective(X, y, trial):
    grid = {
        "n_estimators": trial.suggest_int("n_estimators", 2700, 4500, step=30),
        "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.5, log=True),
        "max_depth": trial.suggest_int("max_depth", 2, 16),
        "subsample": trial.suggest_float("subsample", 0.2, 1.0),
    }
    model = GradientBoostingRegressor(**grid, random_state=0)
    kf = KFold(n_splits=3, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=kf, scoring="neg_mean_absolute_error", n_jobs=-1)
    return float(-scores.mean())

def train_model_and_predict(train_file: str, test_file: str) -> ndarray:
    """
    This function reads dataset stored in the folder, trains predictor and returns predictions.
    :param train_file: the path to the training dataset
    :param test_file: the path to the testing dataset
    :return: predictions for the test file in the order of the file lines (ndarray of shape (n_samples,))
    """

    df_train = pd.read_json(train_file, lines=True)
    df_test = pd.read_json(test_file, lines=True)
    for column in ["potions", "questions", "runtime", "critics_liked", "preorders", "release_year"]:
        df_train.fillna({column: df_train[column].mean()}, inplace=True)
        df_test.fillna({column: df_test[column].mean()}, inplace=True)


    df_train, df_test = tfidf(df_train, df_test, 'keywords', 'k', max_features=50)
    df_train, df_test = tfidf(df_train, df_test, 'genres', 'g', max_features=20)
    df_train, df_test = tfidf(df_train, df_test, 'directors', 'd', max_features=20)
    #df_train, df_test = tfidf_columns(df_train, df_test, 'filming_locations', 'loc', max_features=20)
    for column in ['filming_locations']: # вроде не супер нужная штука
        del df_train[column]
        del df_test[column]
    for i in range(3):
        del df_train[f"actor_{i}_gender"]
        # del df_train[f"actor_{i}_postogramm"]
        del df_test[f"actor_{i}_gender"]
        # del df_test[f"actor_{i}_postogramm"]

    y_train = df_train["awards"]
    del df_train["awards"]
    # print(list(df_train.columns))

    study = optuna.create_study(direction="minimize")
    study.optimize(lambda trial: objective(df_train, y_train, trial), n_trials=10, n_jobs=-1)
    best_params = study.best_params

    regressor = GradientBoostingRegressor(**best_params, random_state=0)
    # cat_features = ["directors", "filming_locations", "keywords"]
    #regressor = CatBoostRegressor(iterations=1070, learning_rate=0.1, depth=4, verbose=0)
    # regressor.fit(df_train, y_train)
    # return regressor.predict(df_test)
    regressor.fit(df_train.to_numpy(), y_train.to_numpy())
    return regressor.predict(df_test.to_numpy())
