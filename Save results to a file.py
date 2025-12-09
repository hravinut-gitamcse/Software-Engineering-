import math

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


with open(r"C:\Users\DELL\OneDrive\Documents\GITAM\Software Engineering\Quadratic Solver\input(1).txt", "r") as f, \
     open("output.txt", "w", encoding="utf-8") as out:

    for line in f:
        if line.strip():
            a, b, c = map(float, line.split())
            result = solve_quadratic(a, b, c)
            out.write(f"For a={a}, b={b}, c={c} -> {result}\n")

print("Results saved to output.txt")
