from src.atmosphere import calculate_density, calculate_dynamic_pressure
from src.aerodynamics import (
    calculate_lift,
    calculate_drag,
    calculate_lift_to_drag,
    find_max_cl,
    find_max_ld,
    find_min_cd
)
from src.xflr5_reader import read_xflr5_polar, get_coefficients_at_alpha
from src.plotter import plot_cl_vs_alpha, plot_cd_vs_alpha, plot_ld_vs_alpha
from src.polar_analysis import analyze_polar
from src.inputs import get_flight_inputs

altitude, velocity, wing_area, angle_of_attack = get_flight_inputs()

# Atmosphere calculations
density = calculate_density(altitude)
dynamic_pressure = calculate_dynamic_pressure(density, velocity)

# Read XFLR5 polar data
filename = "data/NACA 2412_T1_Re0.100_M0.00_N9.0.txt"
polar = read_xflr5_polar(filename)
polar_results = analyze_polar(polar)

print("\n========== POLAR ANALYSIS ==========")
print("CLmax:", polar_results["cl_max"])
print("AoA @ CLmax:", polar_results["alpha_cl_max"], "deg")
print("CDmin:", polar_results["cd_min"])
print("AoA @ CDmin:", polar_results["alpha_cd_min"], "deg")
print("L/Dmax:", polar_results["ld_max"])
print("AoA @ L/Dmax:", polar_results["alpha_ld_max"], "deg")
print("====================================")
# stall_angle, cl_max = find_max_cl(polar)
# best_ld_angle, max_ld = find_max_ld(polar)
# min_cd_angle, cd_min = find_min_cd(polar)

plot_cl_vs_alpha(polar)
plot_cd_vs_alpha(polar)
plot_ld_vs_alpha(polar)

coefficients = get_coefficients_at_alpha(polar, angle_of_attack)

cl = coefficients[0]
cd = coefficients[1]
cm = coefficients[2]

# Calculate aerodynamic forces
lift = calculate_lift(dynamic_pressure, wing_area, cl)
drag = calculate_drag(dynamic_pressure, wing_area, cd)
lift_to_drag = calculate_lift_to_drag(lift, drag)

# Display results
print("Altitude:", altitude, "m")
print("Velocity:", velocity, "m/s")
print("Density:", density, "kg/m^3")
print("Dynamic Pressure:", dynamic_pressure, "Pa")

print("Angle of Attack:", angle_of_attack, "deg")
print("CL:", cl)
print("CD:", cd)
print("Cm:", cm)

print("Lift:", lift, "N")
print("Drag:", drag, "N")
print("L/D Ratio:", lift_to_drag)