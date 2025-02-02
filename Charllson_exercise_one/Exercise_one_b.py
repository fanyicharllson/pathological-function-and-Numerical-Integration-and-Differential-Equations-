# Calculate the first and second derivatives

import sympy as sp #for symbolic math
import numpy as np #for numerical operations
import matplotlib.pyplot as plt #for plotting

# Define the symbol x, k
x, k = sp.symbols('x k')

# Define the function f(x)
f = sp.Sum(sp.sin(k**2 * x) / k**5, (k, 1, 100))

# Calculate derivatives using sympy
f_prime = sp.diff(f.doit(), x)
f_double_prime = sp.diff(f_prime, x)

# Lambdify the derivatives for plotting
f_prime_lambdified = sp.lambdify(x, f_prime, modules=["numpy"])
f_double_prime_lambdified = sp.lambdify(x, f_double_prime, modules=["numpy"])

# Define x values for plotting
x_vals = np.linspace(-10, 10, 1000)

# Calculate derivative values
f_prime_vals = f_prime_lambdified(x_vals)
f_double_prime_vals = f_double_prime_lambdified(x_vals)

# Plot the derivatives
plt.figure(figsize=(12, 6))
plt.plot(x_vals, f_prime_vals, label="First Derivative f'(x)", color='blue')
plt.plot(x_vals, f_double_prime_vals, label="Second Derivative f''(x)", color='orange')
plt.title('Exercise One b: Derivatives of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
