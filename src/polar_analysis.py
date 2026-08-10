def analyze_polar(polar_data):

    max_cl_point = max(polar_data, key=lambda row: row[1])
    min_cd_point = min(polar_data, key=lambda row: row[2])

    max_ld_point = max(
        polar_data,
        key=lambda row: row[1] / row[2]
    )

    return {
        "cl_max": max_cl_point[1],
        "alpha_cl_max": max_cl_point[0],

        "cd_min": min_cd_point[2],
        "alpha_cd_min": min_cd_point[0],

        "ld_max": max_ld_point[1] / max_ld_point[2],
        "alpha_ld_max": max_ld_point[0]
    }