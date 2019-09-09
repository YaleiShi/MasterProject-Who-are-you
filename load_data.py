import pandas as pd
import numpy as np
import glob
import os


train_x = []
train_y = []
test_x = []
test_y = []



def load_train_x():
    path = "./mfcc/append_train/"

    for filename in os.listdir(path):
        if filename.endswith('.npy'): 
            mfcc = np.load(path + filename)
            train_x.append(stupid_keras_d3_to_d4(mfcc))

def load_test_x():
    path = "./mfcc/append_test/"

    for filename in os.listdir(path):
        if filename.endswith('.npy'): 
            mfcc = np.load(path + filename)
            test_x.append(stupid_keras_d3_to_d4(mfcc))

def load_train_y():
    train_y = pd.read_csv("./data/feature_reduced_30_train_Y.csv").values[:, 1]
    # print(train_y)
    return train_y

def load_test_y():
    test_y = pd.read_csv("./data/feature_reduced_30_test_Y.csv").values[:, 1]
    # print(test_y)
    return test_y

def stupid_keras_d3_to_d4(data):
    data4 = np.zeros((20, 1241, 1))
    for i in range(0, 20):
        for j in range(0, 1241):
            data4[i][j][0] = data[i][j]
    return data4

load_train_x()
train_y = load_train_y()
load_test_x()
test_y = load_test_y()

# print("train_y, ", train_y)
# print("test_y, ", test_y)
print("shape of train_x" ,np.shape(train_x))
print("shape of train_y" ,np.shape(train_y))
print("shape of test_x" ,np.shape(test_x))
print("shape of test_y" ,np.shape(test_y))
