import numpy as np
import scipy.constants as const

# Masses Earth and Moon
M_earth = const.earth.mass
M_moon = const.moon.mass

# Distance between centers Earth and Moon (Radius Moon + Radius Earth)
R = const.moon.equatorial_radius + const.earth.equatorial_radius

# Gravitational constant
G = const.gravitational_constant

# Force of gravitational attraction
F = G * M_earth * M_moon / R**2
print(F)