# Agile Model: Weather Prediction

import matplotlib.pyplot as plt

def predict_weather(a, b, c):
    days = range(0, 8)
    temps = [a*d*d + b*d + c for d in days]
    return days, temps

# Sprint 1
a, b, c = -1.9, 2.4, 3.1
days, temps = predict_weather(a, b, c)

print("Sprint Output:")
for d, t in zip(days, temps):
    print(f"Day {d}: {t:.2f} °C")

# Sprint 2: User feedback (changed coefficient)
a = -0.4
days, temps = predict_weather(a, b, c)

# Diagram
plt.plot(days, temps, marker='o')
plt.title("Weather Modeling - Agile")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.savefig("agile_weather_model.png")
plt.show()
