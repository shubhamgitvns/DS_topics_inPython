import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 60)
y = np.linspace(-4, 4, 60)

X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_wireframe(X, Y, Z)

ax.set_title("3D Wireframe Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()