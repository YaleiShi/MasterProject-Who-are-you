import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
# from sklearn.externals import joblib
import joblib
from scipy.stats import spearmanr
from scipy.stats import pearsonr

# lead the data set
# train = pd.read_csv("./data/training.csv")
print("reading data ... ")
test = pd.read_csv("./data/test.csv")
# remove the first column which is the index (0 1 2 3), remove the secound column which is the audio name
# del train['name']
del test['name']
# seperate the final score to get X and Y
# create training_X training_Y test_X test_Y 
# training_Y = train['pros'].as_matrix()
test_Y = test['pros'].as_matrix()

# del train['pros']
del test['pros']
# training_X = train.as_matrix()
test_X = test.as_matrix()

# load the model from disk
print("opening model ... ")
model = joblib.load("./model/svrModel.pkl")

print("predicting result ... ")
test_predict_Y = model.predict(test_X)
# error rate on training data
# mse = mean_absolute_error(training_Y, model.predict(training_X))
# print("mean_absolute_error of training data is: %.4f" % mse)

# error rate on test data
# mse = mean_absolute_error(test_Y, model.predict(test_X))
# print("mean_absolute_error of training data is: %.4f" % mse)

# test data spearman
corr, p_value = spearmanr(test_Y, test_predict_Y)
print("test data spearman corealation is: %.4f" % corr)
print("test data spearman p value is: %.4f" % p_value)

# test data pearson
corr, p_value = pearsonr(test_Y, test_predict_Y)
print("test data pearson corealation is: %.4f" % corr)
print("test data pearson p value is: %.4f" % p_value)