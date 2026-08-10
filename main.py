from src.atmosphere import calculate_density, calculate_dynamic_pressure
from src.aerodynamics import calculate_lift

altitude = 1000
velocity = 20

density = calculate_density(altitude)
dynamic_pressure = calculate_dynamic_pressure(density, velocity)

wing_area = 0.4
cl = 0.8

lift = calculate_lift(dynamic_pressure, wing_area, cl)

print("Density:", density, "kg/m^3")
print("Dynamic Pressure:", dynamic_pressure, "Pa")
print("Lift:", lift, "N")