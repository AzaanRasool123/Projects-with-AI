import math

def calculate_trig(angle, unit, trig_type):
    if unit == 'degrees':
        angle_in_radians = math.radians(angle)
    elif unit == 'radians':
        angle_in_radians = angle
    else:
        return "Invalid unit. Please enter 'degrees' or 'radians'."

    if trig_type == 'sin':
        return math.sin(angle_in_radians)
    elif trig_type == 'cos':
        return math.cos(angle_in_radians)
    elif trig_type == 'tan':
        return math.tan(angle_in_radians)
    else:
        return "Invalid trig type. Please enter 'sin', 'cos', or 'tan'."

def main():
    print("Trigonometric Calculator")
    print("------------------------")

    angle = float(input("Enter the angle: "))
    unit = input("Enter the unit (degrees or radians): ")
    trig_type = input("Enter the trig type (sin, cos, or tan): ")

    result = calculate_trig(angle, unit, trig_type)

    print(f"The {trig_type} of {angle} {unit} is {result:.4f}")

if __name__ == "__main__":
    main()