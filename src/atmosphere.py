def calculate_density(altitude):
    T0 = 288.15
    P0 = 101325
    R = 287.05
    L = 0.0065
    g = 9.80665

    temperature = T0 - L * altitude

    pressure = P0 * (temperature / T0) ** (g / (R * L))

    density = pressure / (R * temperature)

    return density

def calculate_dynamic_pressure(density, velocity):
    dynamic_pressure = 0.5 * density * velocity**2

    return dynamic_pressure