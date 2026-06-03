import matplotlib.pyplot as plt
import numpy as np

# Generate random data for three groups
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1, 100)
data3 = np.random.normal(-2, 1, 100)
data = [data1, data2, data3]

# Create a boxplot
fig, ax = plt.subplots()
ax.boxplot(data)

# Add labels and title
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
ax.set_ylabel('Value')
ax.set_title('Boxplot Example')

# Display the plot
plt.show()