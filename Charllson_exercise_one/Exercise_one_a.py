#: A pathological function f(x)
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the symbol x
x, k = sp.symbols('x k')

# Define the summation function
f = sp.Sum(sp.sin(k**2 * x) / k**5, (k, 1, 100))

# Lambdify the function for plotting
f_lambdified = sp.lambdify(x, f.doit(), modules=["numpy"])

# Define x values for plotting
x_vals = np.linspace(-10, 10, 1000)

# Calculate f(x) values
f_vals = f_lambdified(x_vals)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(x_vals, f_vals, label=r'$f(x) = \sum_{k=1}^{100} \frac{\sin(k^2x)}{k^5}$')
plt.title('Exercise One a: Graph of the Function f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
