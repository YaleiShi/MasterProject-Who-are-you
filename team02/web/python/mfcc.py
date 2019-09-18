from __future__ import print_function
import numpy as np
import scipy
import matplotlib.pyplot as plt

import librosa
import librosa.display

y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)
#y, sr = librosa.load("./tool.mp3", offset=30, duration=5)

result = librosa.feature.mfcc(y=y, sr=sr)

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000)

result2 = librosa.feature.mfcc(S=librosa.power_to_db(S))


mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=100)

print(sr)
#x = np.arange(6000)
#plt.plot(x, y[600:6600])

#plt.show()
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')

plt.tight_layout()
plt.savefig('mfcc.png')
