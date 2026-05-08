import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(1, 2, 3)

ax.set_title("My First 3D Point")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.show()