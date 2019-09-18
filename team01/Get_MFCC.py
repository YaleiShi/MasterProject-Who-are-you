from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np
import os
import librosa

# directory where we your .wav files are
directoryName = "./" # put your own directory here
# directory to put our results in, you can change the name if you like
resultsDirectory = "../mfcc"
testDirectory = resultsDirectory + "/test"
trainDirectory = resultsDirectory + "/train"

# make a new folder in this directory to save our results in 
if not os.path.exists(resultsDirectory):
    os.makedirs(resultsDirectory)
if not os.path.exists(testDirectory):
    os.makedirs(testDirectory)
if not os.path.exists(trainDirectory):
    os.makedirs(trainDirectory)

# get MFCCs for every .wav file in our specified directory 
for filename in os.listdir(directoryName):
    if filename.endswith('.wav'): 
        y, sr = librosa.load(directoryName + "/" +filename)

        # Compute MFCC features from the raw signal
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

        if 'test' in filename:
            outputFile = testDirectory + "/" + os.path.splitext(filename)[0] + ".npy"
        if 'train' in filename:
            outputFile = trainDirectory + "/" + os.path.splitext(filename)[0] + ".npy"

        file = open(outputFile, 'w+') # make file/over write existing file
        np.save(outputFile, mfcc)
        file.close() # close file