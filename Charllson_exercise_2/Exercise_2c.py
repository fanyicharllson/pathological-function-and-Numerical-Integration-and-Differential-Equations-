from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Define the first differential equation x'(t) = 1 + t^2 - x(t)^2
def eq1(t, x):
    return 1 + t**2 - x**2

# Define the second set of differential equations
def eq2(t, y):
    dydt = [y[1], y[1]/2 - y[0] - y[1]**3]
    return dydt

# Solve eq1
sol1 = solve_ivp(eq1, [0, 40], [0], t_eval=np.linspace(0, 40, 1000))

# Solve eq2
sol2 = solve_ivp(eq2, [0, 40], [0, 1], t_eval=np.linspace(0, 40, 1000))

# Plot the solutions
plt.figure(figsize=(15, 6))

# Plot x'(t)
plt.subplot(1, 2, 1)
plt.plot(sol1.t, sol1.y[0], label='x(t)', color='red')
plt.title("Solution of x'(t)")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid()

# Plot second differential equation solutions
plt.subplot(1, 2, 2)
plt.plot(sol2.t, sol2.y[0], label='y1(t)', color='blue')
plt.plot(sol2.t, sol2.y[1], label='y2(t)', color='green')
plt.title("Solutions of Second Differential Equation")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
