import pandas as pd
import numpy as np
import glob
import os
import timit



f = open("48_new.txt")
target = f.read().splitlines()
f.close()

map48 = {}

for i, val in enumerate(target):
    map48[val] = i

print("target: ", target)

def target_array(p):
    listofzeros = [0] * len(target)
    listofzeros[map48[p]] = 1
    return listofzeros



train_x = []
train_y = []
test_x = []
test_y = []





def load_mfcc_from_file(path):
    df=pd.read_csv(path, sep=' ',header=None)
    data = df.values
    size = len(data)

    for x in range(12, size - 12):
        phone = data[x][2]
        if phone in target :
            window = stupid_keras_d3_to_d4(data[x-12:x+13, 3:43])
            train_x.append(window)
            train_y.append(target_array(phone))


def load_mfcc_from_file_for_test(path):
    df=pd.read_csv(path, sep=' ',header=None)
    data = df.values
    size = len(data)

    for x in range(12, size - 12):
        phone = data[x][2]
        if phone in target :
            window = stupid_keras_d3_to_d4(data[x-12:x+13, 3:43])
            test_x.append(window)
            test_y.append(target_array(phone))




def stupid_keras_d3_to_d4(data):
    data4 = np.zeros((1, 25, 40))
    for i in range(0, 25):
        for j in range(0, 40):
            data4[0][i][j] = data[i][j]
    return data4





# path = timit.TIMIT_PATH + "/TRAIN"
# pattern = os.path.join(path, "*/*/*.mfcc")
path = timit.TIMIT_PATH + "/TRAIN/DR7/FBLV0" ;
pattern = os.path.join(path, "*.spec1")
files = glob.glob(pattern)

count = 0
for f in files:
    print(count, "  >>> processing ", f)
    load_mfcc_from_file(f)
    count += 1


path = timit.TIMIT_PATH + "/TEST"
pattern = os.path.join(path, "DR1/FAKS0/SX43.mfcc")
files = glob.glob(pattern)

count = 0
for f in files:
    print(count, "  >>> processing test ", f)
    load_mfcc_from_file_for_test(f)
    count += 1


# print("shape of train_x" ,np.shape(train_x))
# print("shape of train_y" ,np.shape(train_y))
# print("shape of test_x" ,np.shape(test_x))
# print("shape of test_y" ,np.shape(test_y))

print("shape of train_x" ,np.shape(train_x))
#np.save('train_x_p.txt', train_x)
print("shape of train_y" ,np.shape(train_y))
#np.save('train_y_p.txt', train_y)
print("shape of test_x" ,np.shape(test_x))
np.save('test_x_p.txt', test_x)
print("shape of test_y" ,np.shape(test_y))
np.save('test_y_p.txt', test_y)
