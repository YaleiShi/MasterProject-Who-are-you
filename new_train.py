import pandas as pd
import numpy as np
from sklearn.svm import SVR
from scipy.stats import spearmanr
from scipy.stats import pearsonr

df=pd.read_csv('./data/training.csv', sep=',',header=None)
m = df.values
train_x = m[:,1:6000]
train_y = m[:,11153]

df2=pd.read_csv('./data/test.csv', sep=',',header=None)
m2 = df2.values
test_x = m2[:,1:6000]
test_y = m2[:,11153]


clf = SVR(kernel='poly', gamma='scale', C= 1000, epsilon = 0.0001)


clf.fit(train_x, train_y)

prod_y = clf.predict(test_x)


# for i in range(len(test_y)):
#     print(test_y[i], prod_y[i])



corr, p_value = spearmanr(test_y, prod_y)
print("test data spearman corealation is: %.4f" % corr)
print("test data spearman p value is: %.4f" % p_value)

# test data pearson
corr, p_value = pearsonr(test_y, prod_y)
print("test data pearson corealation is: %.4f" % corr)
print("test data pearson p value is: %.4f" % p_value)
