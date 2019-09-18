# Plot a monophonic waveform
from __future__ import print_function
import numpy as np
import scipy
import matplotlib.pyplot as plt

import librosa
import librosa.display

y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)

print(np.shape(y))

(x,) = np.shape(y)
totalTime = x / sr;
x = np.linspace(0, totalTime, x)

plt.figure(figsize=(10, 2))

# librosa.display.waveplot(y, sr=sr)
# plt.title('Monophonic')
#
# plt.savefig('wave.png')
