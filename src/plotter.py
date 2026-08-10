import matplotlib.pyplot as plt

def plot_cl_vs_alpha(polar_data):
    alpha = [row[0] for row in polar_data]
    cl = [row[1] for row in polar_data]

    max_point = max(polar_data, key=lambda row: row[1])
    max_alpha = max_point[0]
    max_cl = max_point[1]

    plt.plot(alpha, cl)
    plt.scatter(max_alpha, max_cl)

    plt.xlabel("Angle of Attack (deg)")
    plt.ylabel("Lift Coefficient (CL)")
    plt.title("CL vs Angle of Attack")
    plt.grid()

    plt.annotate(
        f"CLmax = {max_cl}\nAoA = {max_alpha}°",
        (max_alpha, max_cl)
    )

    plt.show()

def plot_cd_vs_alpha(polar_data):
    alpha = [row[0] for row in polar_data]
    cd = [row[2] for row in polar_data]

    plt.plot(alpha, cd)

    plt.xlabel("Angle of Attack (deg)")
    plt.ylabel("Drag Coefficient (CD)")
    plt.title("CD vs Angle of Attack")
    plt.grid()

    plt.show()

def plot_ld_vs_alpha(polar_data):
    alpha = [row[0] for row in polar_data]
    cl = [row[1] for row in polar_data]
    cd = [row[2] for row in polar_data]

    ld = [cl_value / cd_value for cl_value, cd_value in zip(cl, cd)]

    max_index = ld.index(max(ld))
    max_ld = ld[max_index]
    max_alpha = alpha[max_index]

    plt.plot(alpha, ld)
    plt.scatter(max_alpha, max_ld)

    plt.xlabel("Angle of Attack (deg)")
    plt.ylabel("Lift-to-Drag Ratio (L/D)")
    plt.title("L/D vs Angle of Attack")
    plt.grid()

    plt.annotate(
        f"L/Dmax = {max_ld:.2f}\nAoA = {max_alpha}°",
        (max_alpha, max_ld)
    )

    plt.show()