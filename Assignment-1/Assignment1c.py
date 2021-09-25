from sklearn.datasets import make_moons
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 4)
gs.update(wspace=0.5)
plt.show()

# Make Moons
plt.subplot(gs[0, :2], )
plt.title("make_moons random dataset plot")

X1, y1 = make_moons(n_samples=100, noise=0.1)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=y1, s=25, edgecolor='k')

# Make Circles
plt.subplot(gs[0, 2:])
plt.title("make_circles random dataset plot")

X2, y2 = make_circles(n_samples=100, noise=0.05)
plt.scatter(X2[:, 0], X2[:, 1], marker='o', c=y2, s=25, edgecolor='k')

# Make Blobs
plt.subplot(gs[1, 1:3])
plt.title("make_blobs random dataset plot")

X3, y3 = make_blobs(n_samples=100, centers=4, n_features=2)
plt.scatter(X3[:, 0], X3[:, 1], marker='o', c=y3, s=25, edgecolor='k')
plt.show()