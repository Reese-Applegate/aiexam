import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the quasi-monochromatic dipole spectrum
wavelengths = np.linspace(400, 700, 1000)  # Wavelengths in nm
center_wavelength = 532  # Center wavelength in nm (typical for green laser)
linewidth = 5  # Slightly broader linewidth for quasi-monochromatic light
amplification_factor = 50  # High amplification factor for light intensity

# Define space (x) and fix time (t = constant)
x = np.linspace(-10, 10, 500)  # Space in arbitrary units
t_fixed = 10  # Fix time to a constant value

# Lorentz transformation parameters
beta = 0.5  # Velocity as a fraction of the speed of light (v/c)
gamma = 1 / np.sqrt(1 - beta**2)  # Lorentz factor

# Apply Lorentz transformation to space coordinates (time is fixed)
X_prime = gamma * (x - beta * t_fixed)  # Transformed space
T_prime = gamma * (t_fixed - beta * x)  # Transformed time (constant)

# Simulate the energy spectrum as a function of space
spectrum = (
    amplification_factor
    * (linewidth**2)
    / ((wavelengths - center_wavelength) ** 2 + linewidth**2)
)

# Apply smoother modulation for Wolf effect
modulation = 0.1 * np.sin(
    2 * np.pi * X_prime / 20
)  # Reduced amplitude and longer wavelength
space_energy_spectrum = (
    (1 + modulation) * np.exp(-(X_prime**2) / 40) * spectrum[500]
)  # Smoother decay

# Plot the space-energy spectrum
plt.figure(figsize=(10, 6))
plt.plot(
    X_prime, space_energy_spectrum, label="Energy Spectrum (Wolf Effect)", color="blue"
)
plt.title("Space-Energy Spectrum with Wolf Effect (Smoothed)")
plt.xlabel("Transformed Space (arbitrary units)")
plt.ylabel("Energy Intensity (a.u.)")
plt.grid(True)
plt.legend()
plt.show()
