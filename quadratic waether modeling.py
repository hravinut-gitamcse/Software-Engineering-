import math

# Function to solve quadratic equation
def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"Two real solutions: {x1}, {x2}"

    elif D == 0:
        x = -b / (2*a)
        return f"One real solution: {x}"

    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        return f"Complex solutions: {real}+{imag}i , {real}-{imag}i"

# Manual input only
print("Quadratic Equation Solver")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

result = solve_quadratic(a, b, c)
print(result)