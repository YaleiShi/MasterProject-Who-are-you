# Feature Importance with Extra Trees Classifier
from pandas import read_csv
import pandas as pd
from sklearn import tree
import numpy as np
import joblib
from sklearn.feature_selection import SelectFromModel

# load data
print("reading files ... ")
train = pd.read_csv("./data/training.csv")
test = pd.read_csv("./data/test.csv")
train_array = train.values
test_array = test.values

train_Y = train_array[:, 11153]
train_X = train_array[:, 1 : 11153]

test_Y = test_array[:, 11153]
test_X = test_array[:, 1 : 11153]

# feature extraction
print("training ...")
model = tree.DecisionTreeRegressor()
model.fit(train_X, train_Y)

selection = SelectFromModel(model, threshold=0.0018, prefit=True)

select_train_X = selection.transform(train_X)
select_test_X = selection.transform(test_X)

pd.DataFrame(select_train_X).to_csv("./data/feature_reduced_30_train_X.csv")
pd.DataFrame(select_test_X).to_csv("./data/feature_reduced_30_test_X.csv")
pd.DataFrame(train_Y).to_csv("./data/feature_reduced_30_train_Y.csv")
pd.DataFrame(test_Y).to_csv("./data/feature_reduced_30_test_Y.csv")
# print(np.sort(model.feature_importances_))

joblib.dump(model, "./model/featureSelect.pkl")