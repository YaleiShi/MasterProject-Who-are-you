import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
z = np.linspace(0, 100, 100)

ax.plot(x, y, z, label='parametric curve')
ax.set_xlabel("x arrow", fontsize=10)
ax.set_ylabel("y arrow", fontsize=10)
ax.legend()

plt.show()
