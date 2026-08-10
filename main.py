from src.atmosphere import calculate_density, calculate_dynamic_pressure
from src.aerodynamics import calculate_lift, calculate_drag

altitude = 1000
velocity = 20

density = calculate_density(altitude)
dynamic_pressure = calculate_dynamic_pressure(density, velocity)

wing_area = 0.4
cl = 0.8

lift = calculate_lift(dynamic_pressure, wing_area, cl)

cd = 0.05
drag = calculate_drag(dynamic_pressure, wing_area, cd)

print("Density:", density, "kg/m^3")
print("Dynamic Pressure:", dynamic_pressure, "Pa")
print("Lift:", lift, "N")
print("Drag:", drag, "N")