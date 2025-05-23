import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.38e-23  # Boltzmann constant (J/K)
hbar = 1.05e-34  # Reduced Planck's constant (J·s)
m = 1.44e-25  # Mass of a Rubidium-87 atom (kg)
V = 1e-6  # Volume of the system (m^3)
T_c = 1e-6  # Critical temperature (K)


# Functions
def bose_distribution(energy, T):
    """Bose-Einstein distribution function."""
    if T <= 0:
        T = 1e-12  # Prevent division by zero
    return 1 / (np.exp(energy / (k_B * T)) - 1)


def critical_density(T):
    """Critical density for Bose-Einstein condensation."""
    if T <= 0:
        return 0  # Prevent invalid calculation
    return (2.612 / (2 * np.pi * hbar**2 / m) ** (3 / 2)) * (k_B * T) ** (3 / 2)


# Energy levels
energy = np.linspace(1e-25, 1e-20, 500)  # Avoid zero energy to prevent division issues

# Time evolution parameters
time_steps = np.linspace(0, 1, 100)  # Simulated time steps (arbitrary units)
temperatures = T_c * (1 - time_steps)  # Temperature decreases over time

# Plot
plt.figure(figsize=(10, 6))

for i, T in enumerate(temperatures):
    distribution = bose_distribution(energy, T)
    if T < T_c:
        plt.fill_between(
            energy, distribution, color="blue", alpha=0.1
        )  # Condensed phase
    else:
        plt.fill_between(
            energy, distribution, color="orange", alpha=0.1
        )  # Non-condensed phase

    if i % 10 == 0:  # Plot every 10th step for clarity
        plt.plot(energy, distribution, label=f"T = {T:.2e} K")

plt.axvline(
    x=critical_density(T_c), color="red", linestyle="--", label="Critical Density"
)
plt.title("Bose-Einstein Condensation Over Time")
plt.xlabel("Energy (J)")
plt.ylabel("Occupation Number")
plt.legend()
plt.grid()
plt.show()
