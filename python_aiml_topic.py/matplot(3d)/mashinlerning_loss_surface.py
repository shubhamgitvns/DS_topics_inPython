import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-5, 5, 100)
b = np.linspace(-5, 5, 100)

W, B = np.meshgrid(w, b)

Loss = (W - 2)**2 + (B - 1)**2

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(W, B, Loss, cmap="viridis")

ax.set_title("Machine Learning Loss Surface")
ax.set_xlabel("Weight")
ax.set_ylabel("Bias")
ax.set_zlabel("Loss")

plt.show()
