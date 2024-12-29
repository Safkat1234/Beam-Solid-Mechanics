import numpy as np
import matplotlib.pyplot as plt

# Inputs
E = float(input("Enter Young's Modulus of Beam Material in MPa: ")) * 1e3  # Convert MPa to N/mm²
L1 = float(input("Enter Length of Beam in mm: "))
d = float(input("Enter Diameter of Beam in mm: "))
P = float(input("Enter Force Acting at the End of the Beam in N: "))

# Calculations
L = np.linspace(0, L1, 1000)  # Length divided into 1000 equal parts
I = (np.pi * d**4) / 64       # Area Moment of Inertia
y = d / 2                     # Distance from Neutral axis of outermost fiber

# Deflection and Stress
deflection = -(P * L**3) / (3 * E * I)  # Cantilever beam deflection
stress = (P * L1 * y) / I               # Bending stress at the outermost fiber (constant along the beam length)

# Deflection Plot
plt.figure(figsize=(10, 6))
plt.plot(L, deflection, color='green', linestyle='--', label='Deflected Beam Profile')
plt.axhline(0, color='black', linestyle='-', label='Original Beam Profile')
plt.xlabel('Length of Beam (mm)')
plt.ylabel('Deflection of Beam (mm)')
plt.title('Beam Deflection')
plt.legend()
plt.grid(color='lightgrey', linestyle='--')
plt.show()

# Stress Plot (Optional)
plt.figure(figsize=(10, 6))
plt.plot([0, L1], [stress, stress], color='blue', linestyle='-', label='Bending Stress')
plt.xlabel('Length of Beam (mm)')
plt.ylabel('Stress (N/mm²)')
plt.title('Bending Stress along Beam Length')
plt.legend()
plt.grid(color='lightgrey', linestyle='--')
plt.show()


