from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV

print("reading data ... ")
# load the data set
X_train = pd.read_csv("./data/feature_reduced_30_train_X.csv").values
Y_train = pd.read_csv("./data/feature_reduced_30_train_Y.csv").values[:, 1]
X_test = pd.read_csv("./data/feature_reduced_30_test_X.csv").values
Y_test = pd.read_csv("./data/feature_reduced_30_test_Y.csv").values[:, 1]

# train the model by svr
print("training ... ")
xgb1 = XGBRegressor()

params = {
    'booster': ['gbtree'],
    'objective': ['reg:gamma', 'reg:linear'],
    'gamma': [100, 10, 1, 0.1, 0.01, 0.001, 0.0001],
    'max_depth': [3, 5, 10, 15, 20],
    'lambda': [3, 5, 7, 10],
    'subsample': [0.7],
    'colsample_bytree': [0.7],
    'min_child_weight': [3, 4, 5, 6],
    'silent': [1],
    'eta': [0.7, 0.5, 0.3, 0.1, 0.03, 0.05, 0.07],
    'seed': [1000],
    'nthread': [4],
}

xgb_grid = GridSearchCV(xgb1,
                        params,
                        cv = 2,
                        n_jobs = 5,
                        verbose=True)


xgb_grid.fit(X_train,
         Y_train)

print("predicting result ... ")
print(xgb_grid.best_score_)
print(xgb_grid.best_params_)
