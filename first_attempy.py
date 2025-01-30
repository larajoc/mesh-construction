from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

import numpy as np
points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
tri = Delaunay(points)

plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')

for j, p in enumerate(points):
    plt.text(p[0]-0.03, p[1]+0.03, j, ha='right')
for j, s in enumerate(tri.simplices):
    p = points[s].mean(axis=0)
    plt.text(p[0], p[1], '#%d' % j, ha='center')
plt.xlim(-0.5, 1.5); plt.ylim(-0.5, 1.5)
plt.show()
