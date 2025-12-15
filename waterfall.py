# Waterfall Model: Weather Prediction using Quadratic Equation

import matplotlib.pyplot as plt

# Step 1: Requirements (fixed values)
a = 1.7
b = -2.6
c = 3.5

# Step 2: Design
def temperature(day):
    return a * day**2 + b * day + c

# Step 3: Implementation
days = list(range(0, 8))
temps = []

for d in days:
    temps.append(temperature(d))

# Step 4: Testing (print output)
for d, t in zip(days, temps):
    print(f"Day {d}: {t:.2f} °C")

# Step 5: Deployment (Diagram for GitHub)
plt.plot(days, temps, marker='o')
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weather Modeling - Waterfall")
plt.grid()
plt.savefig("waterfall_weather_model.png")
plt.show()
