import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from scipy.stats import spearmanr
from scipy.stats import pearsonr

print("reading data ... ")
# # lead the data set
# dataSet = pd.read_csv("./data/grid_search_training.csv")
# # remove the secound column which is the audio name
# del dataSet['name']
# # seperate the final score to get X and Y
# # create training_X training_Y test_X test_Y 
# y = dataSet['pros'].as_matrix()
# del dataSet['pros']
# x = dataSet.as_matrix()
X_train = pd.read_csv("./data/feature_reduced_30_train_X.csv").values
Y_train = pd.read_csv("./data/feature_reduced_30_train_Y.csv").values[:, 1]
X_test = pd.read_csv("./data/feature_reduced_30_test_X.csv").values
Y_test = pd.read_csv("./data/feature_reduced_30_test_Y.csv").values[:, 1]

print(Y_test)

# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state=0)

# train the model by svr
print("training ... ")
model = ensemble.GradientBoostingRegressor(
	n_estimators = 1000,
	learning_rate = 0.1,
	max_depth = 6,
	min_samples_leaf = 9,
	max_features = 0.1,
	loss = 'huber',
	random_state = 0)

model.fit(X_train, Y_train)

# save the model
joblib.dump(model, "./model/GBRModel.pkl")

print("predicting result ... ")
test_predict_Y = model.predict(X_test)

# test data spearman
corr, p_value = spearmanr(Y_test, test_predict_Y)
print("test data spearman corealation is: %.4f" % corr)
print("test data spearman p value is: %.4f" % p_value)

# test data pearson
corr, p_value = pearsonr(Y_test, test_predict_Y)
print("test data pearson corealation is: %.4f" % corr)
print("test data pearson p value is: %.4f" % p_value)