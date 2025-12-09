
import math
with open(r"C:\Users\DELL\OneDrive\Documents\GITAM\Software Engineering\Quadratic Solver\input.txt", "r") as f:
    line = f.readline()
    a, b, c = map(float, line.split())
discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Two real solutions:", x1, x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("One real solution:", x)
else:
    real = -b / (2 * a)
    imag = math.sqrt(-discriminant) / (2 * a)
    print(f"Complex solutions: {real}+{imag}i , {real}-{imag}i")
