import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the first pie chart
labels1 = ['A', 'B', 'C', 'D', 'E']
sizes1 = np.random.randint(1, 50, 5)

# Generate random data for the second pie chart
labels2 = ['F', 'G', 'H', 'I', 'J']
sizes2 = np.random.randint(1, 50, 5)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Create the first pie chart
ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90)
ax1.set_title('Pie Chart 1')

# Create the second pie chart
ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90)
ax2.set_title('Pie Chart 2')

# Display the plot
plt.show()