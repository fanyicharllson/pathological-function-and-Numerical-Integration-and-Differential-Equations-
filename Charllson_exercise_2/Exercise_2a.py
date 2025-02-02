# (a) Solve the equation f(x) = 0 for x.

from scipy.optimize import fsolve
import numpy as np

# Define the equation cos(x) - x = 0
def equation(x):
    return np.cos(x) - x

if __name__ == "__main__":
    # Solve for the root
    root = fsolve(equation, 0)
    print("Root of cos(x) = x:", root[0])


