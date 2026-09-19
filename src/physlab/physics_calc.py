## 전자의 비전하

def calculate_specific_charge(voltage, radius_cm, b_field):
    radius_m = radius_cm / 100
    e_m = (2 * voltage) / (radius_m**2 * b_field**2)
    return e_m

def calculate_magnetic_field(current):
    b_field = 6.93 * (10**-4) * current
    return b_field