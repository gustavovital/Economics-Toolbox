import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = x^2 - 1 for phase analysis
def f(x):
    return x**2 - 1

# Define x values around the equilibrium points -1 and 1
x_vals = np.linspace(-2, 2, 1000)
y_vals = f(x_vals)

# Plot the phase line diagram
plt.figure(figsize=(8, 4))
plt.plot(x_vals, y_vals, label=r'$\dot{x} = x^2 - 1$', color="blue")

# Mark the equilibrium points
plt.plot([-1, 1], [0, 0], 'ro', label="Equilibria")  # Equilibria at x = -1 and x = 1

# Add arrows for direction
# Arrows for x < -1
for x in np.linspace(-1.8, -1.2, 4):
    plt.arrow(x, f(x), 0.1, 0, head_width=0.1, head_length=0.05, fc='green', ec='green')

# Arrows for -1 < x < 1
for x in np.linspace(-0.8, 0.8, 4):
    plt.arrow(x, f(x), -0.1, 0, head_width=0.1, head_length=0.05, fc='red', ec='red')

# Arrows for x > 1
for x in np.linspace(1.2, 1.8, 4):
    plt.arrow(x, f(x), 0.1, 0, head_width=0.1, head_length=0.05, fc='green', ec='green')

# Additional plot settings
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(-1, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(1, color='gray', linestyle='--', linewidth=0.5)
plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')
plt.title('Phase Diagram of $\dot{x} = x^2 - 1$')
plt.legend()
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-2, 2)

# Show plot
plt.show()

##########################

# Define the vector field based on the system of equations
def vector_field(X, Y):
    U = 4 * X
    V = Y
    return U, V

# Create a grid of points
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y)

# Plot the phase diagram
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color="blue")

# Mark the equilibrium point at (0, 0)
plt.plot(0, 0, 'ro', label="Equilibrium at (0, 0)")

# Additional plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Phase Diagram of the System')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Show plot
plt.show()