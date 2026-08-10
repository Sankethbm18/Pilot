from src.atmosphere import calculate_density

for altitude in [0, 1000, 2000, 5000]:
    density = calculate_density(altitude)
    print(altitude, "m:", density, "kg/m^3")