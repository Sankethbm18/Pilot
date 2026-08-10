def calculate_lift(dynamic_pressure, wing_area, cl):
    lift = dynamic_pressure * wing_area * cl
    return lift

def calculate_drag(dynamic_pressure, wing_area, cd):
    drag = dynamic_pressure * wing_area * cd

    return drag