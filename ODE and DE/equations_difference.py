import numpy as np
import matplotlib.pyplot as plt

# Define time steps
t = np.arange(0, 10)

# Initial conditions
x0_values = [1, 2]

# Solutions for each equation
solutions = {
    "(a)": [x0 * (-2)**t for x0 in x0_values],
    "(b)": [x0 * 5**t for x0 in x0_values],
    "(c)": [x0 * np.ones_like(t) for x0 in x0_values],
    "(d)": [x0 * (-1)**t for x0 in x0_values]
}

# Plotting
plt.figure(figsize=(12, 8))

for i, (label, sol) in enumerate(solutions.items(), 1):
    plt.subplot(2, 2, i)
    for x0, y in zip(x0_values, sol):
        plt.plot(t, y, label=f'$x_0 = {x0}$')
    plt.title(f"Solution for {label}")
    plt.xlabel("t")
    plt.ylabel("$x_t$")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()



# Define the function g(y)
def g(y):
    return 6 - y**2

# Define the range of y values for the plot
y_values = np.linspace(-4, 4, 400)

# Calculate corresponding y_{t+1} values
yt_plus_1 = g(y_values)

# Plot y_{t+1} = g(y_t)
plt.plot(y_values, yt_plus_1, label=r"$y_{t+1} = g(y_t) = 6 - y_t^2$", color="blue")

# Plot y_{t+1} = y_t (identity line)
plt.plot(y_values, y_values, label=r"$y_{t+1} = y_t$", color="black", linestyle="--")

# Highlight the steady-state at y = 2
plt.plot(2, g(2), 'ro', label="Steady-state $y^* = 2$")

# Arrows to show direction near y = 2
# Start a few points around y = 2 and iteratively apply g(y) to show movement
for y_start in [2.1, 1.9, 2.5, 1.5]:
    ys = [y_start]
    for _ in range(5):  # apply g 5 times
        ys.append(g(ys[-1]))
    plt.plot(ys[:-1], ys[1:], 'r', alpha=0.7)  # plot steps

# Set plot limits and labels
plt.xlim(-4, 4)
plt.ylim(-10, 10)
plt.xlabel(r"$y_t$")
plt.ylabel(r"$y_{t+1}$")
plt.title("Phase Diagram for $y_{t+1} = 6 - y_t^2$ near $y^* = 2$")
plt.legend()
plt.grid(True)
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.show()