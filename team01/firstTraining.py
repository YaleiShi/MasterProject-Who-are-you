import pandas as pd
from sklearn.svm import SVR
import joblib
from sklearn import ensemble

# lead the data set
train = pd.read_csv("./data/training.csv")
# test = pd.read_csv("./data/test.csv")
# remove the first column which is the index (0 1 2 3), remove the secound column which is the audio name
del train['name']
# del test['name']
# seperate the final score to get X and Y
# create training_X training_Y test_X test_Y 
training_Y = train['pros'].as_matrix()
# test_Y = test['pros'].as_matrix()

del train['pros']
# del test['pros']
training_X = train.as_matrix()
# test_X = test.as_matrix()

# train the model by svr
print("training ... ")
# svr = SVR(gamma='scale', C=1.0, epsilon=0.2)
svr = ensemble.GradientBoostingRegressor(
	n_estimators = 1000,
	learning_rate = 0.1,
	max_depth = 6,
	min_samples_leaf = 9,
	max_features = 0.1,
	loss = 'huber',
	random_state = 0)

svr.fit(training_X, training_Y)

# save the model
joblib.dump(svr, "./model/svrModel.pkl")

