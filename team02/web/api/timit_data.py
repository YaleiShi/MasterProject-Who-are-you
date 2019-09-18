import pandas as pd
import librosa
import numpy as np


def load_word(path):
    print("load word path", path)
    df=pd.read_csv(path, sep=' ',header=None)
    data = df.values
    return data.tolist()

def load_wave(path):
    y, sr = librosa.load(path,  sr=16000)
    (x, ) = np.shape(y)
    totalTime = x/sr;
    x = np.linspace(0, totalTime, x)
    return [x.tolist(), y.tolist()]

def load_phn(path):
    df=pd.read_csv(path, sep=' ',header=None)
    data = df.values
    return data.tolist()

def load_spectrogram(path, start, end):
    y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)
   # Passing through arguments to the Mel filters
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000, hop_length = 160)

    if end == 0 :
        return S.tolist()
    else:
        return S[0:80 , start:end].tolist()
