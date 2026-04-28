import numpy as np
from numpy.polynomial import Polynomial

x = np.array([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], dtype=float)
y = np.array([41, 41, 41, 40, 38, 39,38,35,36,36,39,41,40,41,43,43,43,45,45,45,44], dtype=float)

# Older common style
coeffs = np.polyfit(x, y, 1)
poly_old = np.poly1d(coeffs)
print("np.polyfit slope, intercept:", coeffs)
print("Prediction at x=30:", poly_old(30))

# Modern NumPy polynomial API
model = Polynomial.fit(x, y, deg=1)
print("Scaled-domain model:", model)

# Convert to ordinary power basis if you want readable coefficients
model_power = model.convert()
print("Power-basis coefficients [intercept, slope]:", model_power.coef)
print("Prediction at x=30:", model(30))