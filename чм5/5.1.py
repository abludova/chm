
import numpy as np

def f(x, y):
    return 1 + 2.2 * np.sin(x) + 1.5 * y**2

a, b = 0, 0.5
y0 = 0
h = 0.025  

x_points_euler = np.arange(a, b + h, h)
y_points_euler = np.zeros(len(x_points_euler))
y_points_euler[0] = y0

# Метод Эйлера 2-го порядка
print("Метод Эйлера 2-го порядка\n")
for i in range(1, len(x_points_euler)):
    x = x_points_euler[i-1]
    y = y_points_euler[i-1]
    y_tilde = y + h * f(x, y)  
    y_points_euler[i] = y + h/2 * (f(x, y) + f(x + h, y_tilde))  

for x, y in zip(x_points_euler, y_points_euler):
    print(f"x = {x:.3f}, y = {y:.4f}")

y_points_rk = np.zeros(len(x_points_euler))
y_points_rk[0] = y0

# Метод Рунге-Кутты 4-го порядка
print("\nМетод Рунге-Кутты 4-го порядка\n")
for i in range(0, len(x_points_euler) - 1):
    k1 = f(x_points_euler[i], y_points_rk[i])
    k2 = f(x_points_euler[i] + 0.5*h, y_points_rk[i] + 0.5*k1*h)
    k3 = f(x_points_euler[i] + 0.5*h, y_points_rk[i] + 0.5*k2*h)
    k4 = f(x_points_euler[i] + h, y_points_rk[i] + k3*h)
    y_points_rk[i + 1] = y_points_rk[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

for x, y in zip(x_points_euler, y_points_rk):
    print(f"x = {x:.3f}, y = {y:.4f}")
