import matplotlib.pyplot as plt
import numpy as np

# Define the vector field
def vector_field(X, Y):
    U = -2 * X + Y
    V = X - 2 * Y
    return U, V

# Generate grid for plotting
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y)

# Plot the phase diagram
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color="blue")

# Plot the eigenvector lines
plt.plot([-5, 5], [-5, 5], 'r--', label="Eigenvector (1,1)")
plt.plot([-5, 5], [5, -5], 'g--', label="Eigenvector (1,-1)")

# Mark the equilibrium point at the origin
plt.plot(0, 0, 'ko', label="Equilibrium (0,0)")

# Set labels and titles
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Phase Diagram of the System')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

##import matplotlib.pyplot as plt
##import numpy as np

# Define the vector field based on matrix A = [[3, -2], [2, -2]]
def vector_field(X, Y):
    U = 3 * X - 2 * Y
    V = 2 * X - 2 * Y
    return U, V

# Generate a grid of points for the phase plot
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y)

# Plot the phase diagram with quiver
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color="blue")

# Plot the eigenvector lines
# Eigenvector 1 direction (2,1)
plt.plot([-5, 5], [-2.5, 2.5], 'r--', label="Eigenvector (2,1)")

# Eigenvector 2 direction (1,2)
plt.plot([-5, 5], [-10, 10], 'g--', label="Eigenvector (1,2)")

# Mark the origin
plt.plot(0, 0, 'ko', label="Equilibrium (0,0)")

# Set labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Phase Diagram of the System for Matrix A')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

## import matplotlib.pyplot as plt
## import numpy as np

# Define the vector field based on matrix A
def vector_field(X, Y):
    U = -3 * X + 4 * Y
    V = -2 * X + 1 * Y
    return U, V

# Create a grid of points for the phase plot
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y)

# Plot the phase diagram with quiver
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color="blue")

# Mark the equilibrium point at the origin
plt.plot(0, 0, 'ko', label="Equilibrium (0,0)")

# Set labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Phase Diagram: Stable Spiral for Matrix A')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

##import numpy as np
##import matplotlib.pyplot as plt

# Define the system of differential equations
def system(X, t):
    x, y = X
    dxdt = 2 * y
    dydt = 2 * x
    return [dxdt, dydt]

# Create a grid of points in the phase space
x_values = np.linspace(-3, 3, 20)
y_values = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_values, y_values)
U = 2 * Y  # dx/dt
V = 2 * X  # dy/dt

# Plot the vector field
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color="lightgray")

# Plot trajectories for initial conditions
for y0 in np.linspace(-2, 2, 5):
    for x0 in np.linspace(-2, 2, 5):
        t = np.linspace(0, 2, 100)
        trajectory = np.array([system([x0, y0], ti) for ti in t])
        plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-', alpha=0.5)

# Plot the eigenvectors
eigenvector1 = np.array([1, 1]) * 3
eigenvector2 = np.array([1, -1]) * 3
plt.plot([-eigenvector1[0], eigenvector1[0]], [-eigenvector1[1], eigenvector1[1]], 'r--', label='Eigenvector 1 (unstable)')
plt.plot([-eigenvector2[0], eigenvector2[0]], [-eigenvector2[1], eigenvector2[1]], 'g--', label='Eigenvector 2 (stable)')

# Formatting the plot
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Phase Diagram for the Linearized System around $X_+$")
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the nonlinear system after shifting the origin to X+ = (1, 1)
def nonlinear_system(U, t):
    u, v = U
    dudt = (u + 2) * v
    dvdt = u * (v + 2)
    return [dudt, dvdt]

# Set up a finer grid in the phase space for better vector field resolution
u_values = np.linspace(-1.5, 1.5, 20)
v_values = np.linspace(-1.5, 1.5, 20)
U, V = np.meshgrid(u_values, v_values)

# Calculate the vector field for the shifted system
dU = (U + 2) * V
dV = U * (V + 2)

# Plot the vector field with a lower alpha for clarity
plt.figure(figsize=(10, 10))
plt.quiver(U, V, dU, dV, color="gray", alpha=0.3)

# Set up varied initial conditions closer and slightly farther from the origin
initial_conditions = [
    [0.1, 0.1], [-0.1, -0.1], [0.5, -0.5], [-0.5, 0.5],
    [0.2, -0.2], [-0.2, 0.2], [0.8, 0.1], [0.1, -0.8],
    [-0.8, -0.1], [-0.1, 0.8], [1.0, 1.0], [-1.0, -1.0]
]

# Simulate and plot trajectories for each initial condition
t = np.linspace(0, 10, 1000)  # increase time steps for smoother curves
for ic in initial_conditions:
    trajectory = odeint(nonlinear_system, ic, t)
    plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-', alpha=0.8, linewidth=1.5)

# Mark the shifted equilibrium point
plt.plot(0, 0, 'ro', label="Equilibrium (Shifted)")

# Formatting the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel("$u$")
plt.ylabel("$v$")
plt.title("Improved Phase Diagram for the Nonlinear System Near $X_+ = (1,1)$")
plt.legend()
plt.grid(True)
plt.show()