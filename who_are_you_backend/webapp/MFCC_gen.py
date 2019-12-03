import numpy as np
import os
import librosa
# from python_speech_features import mfcc
# from python_speech_features import logfbank
import scipy.io.wavfile as wav

directory = "./mfcc/"
max_len = 1241

def generate_mfcc(path):
    print(path)
    y, sr = librosa.load(path)

    # Compute MFCC features from the raw signal
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

    outputFile = directory + "test_mfcc.npy"

    file = open(outputFile, 'w+') # make file/over write existing file
    np.save(outputFile, mfcc)
    file.close() # close file

    return outputFile

def force_align(path):
    mfcc = np.load(path)
    new_mfcc = np.zeros((20, max_len))
    for i in range(0, 20):
    #   print(len(mfcc[i]))
        row = mfcc[i]
        row_len = len(row)
        if row_len > max_len:
            row_len = max_len

        for j in range(0, row_len):
            # print(len(row))
            new_mfcc[i][j] = row[j]

        # print("row len: %d", len(row))
    outputFile = directory + "force_align.py"
    # print("mfcc len: ", len(new_mfcc[0]))
    file = open(outputFile, 'w+') # make file/over write existing file
    np.save(outputFile, new_mfcc)
    file.close() # close file

    return outputFile

def get_numpy_mfcc(path):
    x = []
    mfcc = np.load(path,  allow_pickle=true)
    x.append(stupid_keras_d3_to_d4(mfcc))

    return x

def stupid_keras_d3_to_d4(data):
    data4 = np.zeros((20, 1241, 1))
    for i in range(0, 20):
        for j in range(0, 1241):
            data4[i][j][0] = data[i][j]
    return data4
