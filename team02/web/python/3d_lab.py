import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import json



import scipy


import librosa


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)

start = 0;
end = 100;
size = end - start;



X = np.linspace(0, size, size)
Y = np.linspace(0, 128, 128)
X, Y = np.meshgrid(X, Y)




y, sr = librosa.load('../data/SI1027.WAV',  sr=16000)
#y, sr = librosa.load("./tool.mp3", offset=30, duration=5)

result = librosa.feature.mfcc(y=y, sr=sr)

# S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000)
#
# result2 = librosa.feature.mfcc(S=librosa.power_to_db(S))



S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, hop_length=160,
                                    fmax=8000)

Z = X+Y
for i in range(310):
    for j in  range(128):
        if S[j][i] > 2 :

            S[j][i] = 2
            print(S[j][i])


# with open('data.json', 'w') as outfile:
#     json.dump(S.tolist(), outfile)

print(np.shape(Z))
print(np.shape(S))


part = S[:,start:end]
print(np.shape(part))


surf = ax.plot_surface(X, Y, part, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_xlabel("time arrow", fontsize=10)
ax.set_ylabel("frequence arrow", fontsize=10)
ax.legend()

plt.show()
