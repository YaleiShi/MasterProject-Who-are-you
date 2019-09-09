from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
from scipy.stats import spearmanr
from scipy.stats import pearsonr

print("reading data ... ")
# load the data set
X_train = pd.read_csv("./data/feature_reduced_30_train_X.csv").values
Y_train = pd.read_csv("./data/feature_reduced_30_train_Y.csv").values[:, 1]
X_test = pd.read_csv("./data/feature_reduced_30_test_X.csv").values
Y_test = pd.read_csv("./data/feature_reduced_30_test_Y.csv").values[:, 1]

# train the model by svr
print("training ... ")

params = {
    'booster': 'gbtree',
    'objective': 'reg:gamma',
    'gamma': 1,
    'max_depth': 3,
    'lambda': 3,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 4,
    'silent': 1,
    'eta': 0.7,
    'seed': 1000,
    'nthread': 4,
}

plst = params.items()


dtrain = xgb.DMatrix(X_train, Y_train)
num_rounds = 6
model = xgb.train(plst, dtrain, num_rounds)

joblib.dump(model, "./model/XGBoostModel.pkl")

print("predicting result ... ")
dtest = xgb.DMatrix(X_test)
test_predict_Y = model.predict(dtest)

# test data spearman
corr, p_value = spearmanr(Y_test, test_predict_Y)
print("test data spearman corealation is: %.4f" % corr)
print("test data spearman p value is: %.4f" % p_value)

# test data pearson
corr, p_value = pearsonr(Y_test, test_predict_Y)
print("test data pearson corealation is: %.4f" % corr)
print("test data pearson p value is: %.4f" % p_value)
