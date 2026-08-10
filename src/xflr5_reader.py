import numpy as np
def read_xflr5_polar(filename):
    polar_data = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines[11:]:
        values = line.split()

        if len(values) >= 5:
            alpha = float(values[0])
            cl = float(values[1])
            cd = float(values[2])
            cm = float(values[4])

            polar_data.append((alpha, cl, cd, cm))

    return polar_data

def get_coefficients_at_alpha(polar_data, target_alpha):
    alpha = np.array([row[0] for row in polar_data])
    cl = np.array([row[1] for row in polar_data])
    cd = np.array([row[2] for row in polar_data])
    cm = np.array([row[3] for row in polar_data])

    cl_value = np.interp(target_alpha, alpha, cl)
    cd_value = np.interp(target_alpha, alpha, cd)
    cm_value = np.interp(target_alpha, alpha, cm)

    return cl_value, cd_value, cm_value