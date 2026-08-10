from src.atmosphere import calculate_density, calculate_dynamic_pressure
from src.aerodynamics import calculate_lift, calculate_drag
from src.xflr5_reader import read_xflr5_polar, get_coefficients_at_alpha


# Flight conditions
altitude = 1000
velocity = 20

# Aircraft geometry
wing_area = 0.4

# Atmosphere calculations
density = calculate_density(altitude)
dynamic_pressure = calculate_dynamic_pressure(density, velocity)

# Read XFLR5 polar data
filename = "data/NACA 2412_T1_Re0.100_M0.00_N9.0.txt"
polar = read_xflr5_polar(filename)

# Get aerodynamic coefficients at desired angle of attack
angle_of_attack = 5.2
coefficients = get_coefficients_at_alpha(polar, angle_of_attack)

cl = coefficients[0]
cd = coefficients[1]
cm = coefficients[2]

# Calculate aerodynamic forces
lift = calculate_lift(dynamic_pressure, wing_area, cl)
drag = calculate_drag(dynamic_pressure, wing_area, cd)

# Display results
print("Altitude:", altitude, "m")
print("Velocity:", velocity, "m/s")
print("Density:", density, "kg/m^3")
print("Dynamic Pressure:", dynamic_pressure, "Pa")

print("Angle of Attack:", angle_of_attack, "deg")
print("CL:", cl)
print("CD:", cd)
print("Cm:", cm)

print("Lift:", lift, "N")
print("Drag:", drag, "N")