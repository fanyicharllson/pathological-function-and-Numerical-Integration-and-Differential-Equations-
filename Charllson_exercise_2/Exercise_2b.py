
import numpy as np
from scipy.integrate import quad
import math

# Define the function to integrate
def func(t):
    return np.sqrt(1 - t**2)

# Integrate from 0 to 1
I, _ = quad(func, 0, 1)
pi_estimate1 = 4 * I

# Integrate from 0 to 1/2
J, _ = quad(func, 0, 0.5)
pi_estimate2 = 12 * (J - (math.sqrt(3) / 8))

print("Pi estimate using method 1:", pi_estimate1)
print("Pi estimate using method 2:", pi_estimate2)
