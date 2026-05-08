import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 200)

x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(x, y, z)

ax.set_title("3D Spiral Line")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
