import numpy as np
import os

directory = "./mfcc"
train = "/train/"
test = "/test/"
out_train = "/append_train/"
out_test  = "/append_test/"

fileName = "/test_0057.npy"

mfcc = np.load(directory + out_test + fileName)
print(len(mfcc[14]))

# max_len = 0
# for filename in os.listdir(directory + test):
#     if filename.endswith('.npy'): 

#         mfcc = np.load(directory + test + filename)

#         if len(mfcc[0]) > max_len:
#         	max_len = len(mfcc[0])

# print(max_len)
