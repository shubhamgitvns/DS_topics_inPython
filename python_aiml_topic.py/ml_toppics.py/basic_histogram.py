import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.normal(size=100)

# Create a histogram with 20 bins
plt.hist(data, bins=10)

# Add labels and titles
plt.title('Distribution of Random Data')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Display the plot
plt.show()