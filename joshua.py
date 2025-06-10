import numpy as np
from scipy.interpolate import interp1d

# Given data
x = np.array([0, 3, 6])
y = np.array([0, 15, 0])

# Linear interpolation
f_linear = interp1d(x, y, kind='linear')
y_linear = f_linear(2)

# Quadratic interpolation
f_quadratic = interp1d(x, y, kind='quadratic')
y_quadratic = f_quadratic(2)

print(f"Linear interpolation at x = 2: {y_linear:.2f} mm")
print(f"Quadratic interpolation at x = 2: {y_quadratic:.2f} mm")


