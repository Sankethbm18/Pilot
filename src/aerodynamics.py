def calculate_lift(dynamic_pressure, wing_area, cl):
    lift = dynamic_pressure * wing_area * cl
    return lift

def calculate_drag(dynamic_pressure, wing_area, cd):
    drag = dynamic_pressure * wing_area * cd

    return drag

def calculate_lift_to_drag(lift, drag):
    return lift / drag