import numpy as np

def system(x, y, z):
    dydx = z
    dzdx = np.cos(1.5*x + y) + (x - y)
    return dydx, dzdx

def runge_kutta_step(x, y, z, h):
    k1y, k1z = system(x, y, z)
    k2y, k2z = system(x + 0.5*h, y + 0.5*k1y, z + 0.5*k1z)
    k3y, k3z = system(x + 0.5*h, y + 0.5*k2y, z + 0.5*k2z)
    k4y, k4z = system(x + h, y + k3y, z + k3z)
    y_next = y + (k1y + 2*k2y + 2*k3y + k4y) * h / 6
    z_next = z + (k1z + 2*k2z + 2*k3z + k4z) * h / 6
    return y_next, z_next

x0, y0, z0 = 0, 0, 1
h = 0.025
a, b = 0, 0.5

x_values = [x0]
y_values = [y0]
z_values = [z0]

for _ in range(2):
    y_next, z_next = runge_kutta_step(x_values[-1], y_values[-1], z_values[-1], h)
    x_values.append(x_values[-1] + h)
    y_values.append(y_next)
    z_values.append(z_next)

# Метод Адамсат 3 порядка
for i in range(2, int((b - a) / h)):
    x_n = x_values[-1] + h
    f_n, g_n = system(x_values[-1], y_values[-1], z_values[-1])
    f_n1, g_n1 = system(x_values[-2], y_values[-2], z_values[-2])
    f_n2, g_n2 = system(x_values[-3], y_values[-3], z_values[-3])
    
    y_next = y_values[-1] + h * (23*f_n - 16*f_n1 + 5*f_n2) / 12
    z_next = z_values[-1] + h * (23*g_n - 16*g_n1 + 5*g_n2) / 12
    
    x_values.append(x_n)
    y_values.append(y_next)
    z_values.append(z_next)

for x, y in zip(x_values, y_values):
    print(f"x = {x:.3f}, y = {y:.4f}")

    
