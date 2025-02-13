import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system of ODEs
def system(t, y, A, beta, alpha):
    K, C = y
    dK_dt = A * K**beta - C
    dC_dt = - (A * beta / alpha) * K**(beta - 1)
    return [dK_dt, dC_dt]


# Parameters
A = 1.0      # Productivity parameter
beta = 0.5   # Diminishing returns
alpha = 1.0  # Utility curvature parameter
B = 1.0      # Bliss point (not directly used here)

# Define the range for K and C
K_min, K_max = 0.1, 2.0
C_min, C_max = 0.0, 2.0

# Create a grid of points
K_vals = np.linspace(K_min, K_max, 20)
C_vals = np.linspace(C_min, C_max, 20)
K_grid, C_grid = np.meshgrid(K_vals, C_vals)

# Compute the derivatives at each grid point
dK = A * K_grid**beta - C_grid
dC = - (A * beta / alpha) * K_grid**(beta - 1)

# Normalize arrows for better visualization
magnitude = np.sqrt(dK**2 + dC**2)
# To avoid division by zero
magnitude[magnitude == 0] = 1
dK_norm = dK / magnitude
dC_norm = dC / magnitude

# Plot the direction field
plt.figure(figsize=(10, 8))
plt.quiver(K_grid, C_grid, dK_norm, dC_norm, magnitude, pivot='mid', cmap='jet')
plt.xlabel('Capital K')
plt.ylabel('Consumption C')
plt.title('Phase Diagram: Capital vs Consumption')
plt.xlim(K_min, K_max)
plt.ylim(C_min, C_max)

# Plot Capital Nullcline: C = A * K^beta
C_nullcline = A * K_vals**beta
plt.plot(K_vals, C_nullcline, 'r--', label=r'$\frac{dK}{dt} = 0$')

# Initial conditions for trajectories
initial_conditions = [
    [0.5, 0.5],
    [0.5, 1.0],
    [1.0, 0.5],
    [1.5, 1.0],
    [1.0, 1.5]
]

# Time span for simulation
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 200)

# Plot each trajectory
for y0 in initial_conditions:
    sol = solve_ivp(system, t_span, y0, args=(A, beta, alpha), t_eval=t_eval, dense_output=True)
    K_traj, C_traj = sol.y
    plt.plot(K_traj, C_traj, label=f'Trajectory from K0={y0[0]}, C0={y0[1]}')

plt.legend()
plt.grid(True)
plt.colorbar(label='Magnitude of Vector Field')
plt.show()