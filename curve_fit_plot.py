import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
time = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
speed = np.array([3.0, 6.1, 8.8, 12.0, 15.3, 17.9])

# Define a function for the curve fit
def func(t, a, b, c):
    return a * t**2 + b * t + c

# Perform the curve fit
params, covariance = curve_fit(func, time, speed)

# Generate points for the curve
fit_time = np.linspace(1.0, 6.0, 100)
fit_speed = func(fit_time, *params)

# Plotting the data and the curve fit
plt.plot(time, speed, 'o', label='Measured Data')
plt.plot(fit_time, fit_speed, label='Curve Fit')

plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.grid(True)

# Save the plot as an image file
plt.savefig('curve_fit_plot.png')

# Show the plot (optional)
plt.show()
