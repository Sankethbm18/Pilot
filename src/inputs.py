def get_flight_inputs():
    altitude = float(input("Enter altitude (m): "))
    velocity = float(input("Enter velocity (m/s): "))
    wing_area = float(input("Enter wing area (m²): "))
    mass = float(input("Enter aircraft mass (kg): "))
    angle_of_attack = float(input("Enter angle of attack (deg): "))

    return altitude, velocity, wing_area, mass, angle_of_attack