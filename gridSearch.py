import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from scipy.stats import spearmanr
from scipy.stats import pearsonr

print("reading data ... ")
# lead the data set
dataSet = pd.read_csv("./data/grid_search_training.csv")
# remove the secound column which is the audio name
del dataSet['name']
# seperate the final score to get X and Y
# create training_X training_Y test_X test_Y 
y = dataSet['pros'].as_matrix()
del dataSet['pros']
x = dataSet.as_matrix()

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state=0)

# train the model by svr
print("training ... ")
model = SVR(kernel='poly', gamma='scale', C=10000, epsilon=0.0001)
model.fit(X_train, Y_train)

# save the model
joblib.dump(model, "./model/testModel.pkl")

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