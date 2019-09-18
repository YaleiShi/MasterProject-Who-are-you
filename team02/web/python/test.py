from __future__ import print_function
import numpy as np
import scipy


import librosa


y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)
# Passing through arguments to the Mel filters
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000, hop_length= 160)
print(np.shape(S[:,0:40]))
