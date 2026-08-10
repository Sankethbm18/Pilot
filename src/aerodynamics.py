def calculate_lift(dynamic_pressure, wing_area, cl):
    lift = dynamic_pressure * wing_area * cl
    return lift

def calculate_drag(dynamic_pressure, wing_area, cd):
    drag = dynamic_pressure * wing_area * cd

    return drag

def calculate_lift_to_drag(lift, drag):
    return lift / drag

def find_max_cl(polar_data):
    max_point = max(polar_data, key=lambda row: row[1])

    alpha = max_point[0]
    cl_max = max_point[1]

    return alpha, cl_max

def find_max_ld(polar_data):
    max_point = max(
        polar_data,
        key=lambda row: row[1] / row[2]
    )

    alpha = max_point[0]
    ld_max = max_point[1] / max_point[2]

    return alpha, ld_max

def find_min_cd(polar_data):
    min_point = min(polar_data, key=lambda row: row[2])

    alpha = min_point[0]
    cd_min = min_point[2]

    return alpha, cd_min

import math


def calculate_stall_speed(mass, density, wing_area, cl_max):
    weight = mass * 9.81

    stall_speed = math.sqrt(
        (2 * weight) /
        (density * wing_area * cl_max)
    )

    return stall_speed