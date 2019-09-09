import numpy as np
import os

directory = "./mfcc"
train = "/train/"
test = "/test/"
out_train = "/append_train/"
out_test  = "/append_test/"

# fileName = "/train_0001.npy"

# mfcc = np.load(directory + train + fileName)
# print(len(mfcc[19]))

max_len = 1241

for filename in os.listdir(directory + train):
    if filename.endswith('.npy'): 

        mfcc = np.load(directory + train + filename)
        new_mfcc = np.zeros((20, max_len))
        for i in range(0, 20):
        # 	print(len(mfcc[i]))
        	row = mfcc[i]
        	row_len = len(row)

        	
        	for j in range(0, row_len):
        		# print(len(row))
        		new_mfcc[i][j] = row[j]

        	# print("row len: %d", len(row))
        outputFile = directory + out_train + filename
        # print("mfcc len: ", len(new_mfcc[0]))
        file = open(outputFile, 'w+') # make file/over write existing file
        np.save(outputFile, new_mfcc)
        file.close() # close file

        # if len(mfcc[0]) > max_len:
        # 	max_len = len(mfcc[0])
