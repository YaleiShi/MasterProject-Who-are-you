import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.utils import shuffle
from sklearn.metrics import make_scorer


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

estimator=SVR(kernel=['poly', 'linear'])
param_grid={
    'C': [0.1, 1, 100, 1000],
    'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10],
    'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5]
}

def score_func(Y_test, test_predict_Y):
    corr, _ = pearsonr(Y_test, test_predict_Y)
    return corr

scorer = make_scorer(score_func, greater_is_better=True)

gsc = GridSearchCV(estimator, param_grid, cv=5, scoring=scorer, verbose=0, n_jobs=-1)

gsc.fit(X_train, Y_train)
best_params = gsc.best_params_

best_svr = SVR(kernel=best_params["kernel"], C=best_params["C"], epsilon=best_params["epsilon"], gamma=best_params["gamma"],
                coef0=0.1, shrinking=True,
                tol=0.001, cache_size=200, verbose=False, max_iter=-1)



print("Best score: %0.3f" % gsc.best_score_)
print("Best parameters set:")

best_parameters = gsc.best_estimator_.get_params()
for param_name in sorted(param_grid.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))

# save the model
joblib.dump(gsc, "./modle/testModel.pkl")

print("predicting result ... ")
test_predict_Y = gsc.predict(X_test)

# test data spearman
corr, p_value = spearmanr(Y_test, test_predict_Y)
print("test data spearman corealation is: %.4f" % corr)
print("test data spearman p value is: %.4f" % p_value)

# test data pearson
corr, p_value = pearsonr(Y_test, test_predict_Y)
print("test data pearson corealation is: %.4f" % corr)
print("test data pearson p value is: %.4f" % p_value)

