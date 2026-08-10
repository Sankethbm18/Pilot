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