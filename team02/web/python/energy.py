from __future__ import print_function
import numpy as np
import scipy
import matplotlib.pyplot as plt

import librosa
import librosa.display

y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)

librosa.feature.rmse(y=y)
# array([[ 0.   ,  0.056, ...,  0.   ,  0.   ]], dtype=float32)

# Or from spectrogram input

S, phase = librosa.magphase(librosa.stft(y))
rms = librosa.feature.rmse(S=S)

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(rms.T, label='RMS Energy')
plt.xticks([])
plt.xlim([0, rms.shape[-1]])
plt.legend(loc='best')
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
plt.show()

# Use a STFT window of constant ones and no frame centering to get consistent
# results with the RMS energy computed from the audio samples `y`

S = librosa.magphase(librosa.stft(y, window=np.ones, center=False))[0]
librosa.feature.rmse(S=S)
