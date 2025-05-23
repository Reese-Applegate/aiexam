import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Parameters
L = 10  # Length of the bound well
x = np.linspace(0, L, 500)  # Spatial points
t = np.linspace(0, 10, 200)  # Time points
k_min, k_max = 0.5, 8  # Range of wavenumbers

# Create the figure and axis
fig, ax = plt.subplots()
(line,) = ax.plot([], [], label="Dynamic Wave")
ax.set_xlim(0, L)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("x")
ax.set_ylabel("Wave Amplitude")
ax.legend()
ax.set_title("Dynamic Wave with Increasing Wavenumber (Bound Ends)")


# Initialize the line
def init():
    line.set_data([], [])
    return (line,)


# Update the line for each frame
def update(frame):
    time = t[frame]
    # Wavenumber increases periodically to achieve 3 fluctuations
    k = k_min + (k_max - k_min) * (np.sin(2 * np.pi * frame / len(t)) + 1) / 2
    wave = np.sin(k * np.pi * x / L) * np.cos(2 * np.pi * time)  # Bound wave
    line.set_data(x, wave)
    return (line,)


# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# Show the animation
plt.show()
