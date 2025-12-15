# Iterative Model: Weather Prediction

import matplotlib.pyplot as plt

# Initial coefficients
a, b, c = 1, -2.5, 3.9

def temperature(day, a, b, c):
    return a * day**2 + b * day + c

days = range(0, 8)

# Iterations
for iteration in range(1, 4):
    temps = [temperature(d, a, b, c) for d in days]
    print(f"\nIteration {iteration}")
    for d, t in zip(days, temps):
        print(f"Day {d}: {t:.2f} °C")

    # Refining model
    a -= 0.1
    b += 0.2

# Diagram
plt.plot(days, temps, marker='o')
plt.title("Weather Modeling - Iterative")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.savefig("iterative_weather_model.png")
plt.show()
