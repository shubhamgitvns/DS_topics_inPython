import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)


fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(x, y, z)

ax.set_title("3D Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()