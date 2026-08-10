def calculate_lift(dynamic_pressure, wing_area, cl):
    lift = dynamic_pressure * wing_area * cl
    return lift