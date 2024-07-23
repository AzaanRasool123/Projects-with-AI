import math
import cmath

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        solution1 = (-b + math.sqrt(discriminant)) / (2*a)
        solution2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real solutions: x = {solution1} and x = {solution2}"
    elif discriminant == 0:
        solution = -b / (2*a)
        return f"One real solution: x = {solution}"
    else:
        sqrt_discriminant = cmath.sqrt(discriminant)
        solution1 = (-b + sqrt_discriminant) / (2*a)
        solution2 = (-b - sqrt_discriminant) / (2*a)
        return f"Two complex solutions: x = {solution1} and x = {solution2}"

def calculate_turning_point(a, b, c):
    x_turning_point = -b / (2*a)
    y_turning_point = a*x_turning_point**2 + b*x_turning_point + c
    return f"Turning point: ({x_turning_point}, {y_turning_point})"

def main():
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))

    equation = f"{a}x^2 + {b}x + {c} = 0"
    print(f"Equation: {equation}")

    solutions = solve_quadratic_equation(a, b, c)
    print(solutions)

    turning_point = calculate_turning_point(a, b, c)
    print(turning_point)

if __name__ == "__main__":
    main()