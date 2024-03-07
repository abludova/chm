import numpy as np
from scipy.interpolate import lagrange
import sympy as sp

x_values = np.array([1.5, 2.0, 2.5, 3.5])
y_values = np.array([0.99745, 0.9093, 0.59847, 0.14112])

x_target = 1.6

poly = lagrange(x_values, y_values)

def f(x):
    return np.sin(x)

y_lagrange = poly(x_target)

y_analytical = f(x_target)

error_lagrange = np.abs(y_analytical - y_lagrange)

h = 1e-5  
left_derivative = (f(x_target) - f(x_target - h)) / h
right_derivative = (f(x_target + h) - f(x_target)) / h
central_derivative = (f(x_target + h) - f(x_target - h)) / (2 * h)

exact_derivative = np.cos(x_target)

results = {
    "Значение в точке X по многочлену Лагранжа": y_lagrange,
    "Аналитическое значение в точке X": y_analytical,
    "Ошибка метода Лагранжа в точке X": error_lagrange,
    "Левая производная в точке X": left_derivative,
    "Правая производная в точке X": right_derivative,
    "Средняя производная в точке X": central_derivative,
    "Точная производная в точке X": exact_derivative
}

formatted_results = {key: f"{value:.6f}" if isinstance(value, float) else value for key, value in results.items()}

for key, value in formatted_results.items():
    print(f"{key}: {value}")
    
#1.2
xk = np.array([1.00, 1.08, 1.20, 1.27, 1.31, 1.38])
yk = np.array([1.17520, 1.30254, 1.50946, 1.21730, 1.22361, 1.23470])

x_star = 1.026

def aitken_interpolation(x_points, y_points, x):
    n = len(x_points)
    pi = np.copy(y_points)
    for k in range(1, n):
        for i in range(n - k):
            pi[i] = ((x - x_points[i + k]) * pi[i] + (x_points[i] - x) * pi[i + 1]) / (x_points[i] - x_points[i + k])
    return pi[0]

y_star_aitken = aitken_interpolation(xk, yk, x_star)

y_star_aitken_formatted = f"{y_star_aitken:.6f}"
print("Значение в точке х:", y_star_aitken_formatted)

#2

import numpy as np
from scipy.interpolate import BarycentricInterpolator

def f(x):
    return np.log(x / 2)

x_nodes = np.linspace(4.5, 10, 5)
y_points = f(x_nodes)

m = 5.03

interpolator = BarycentricInterpolator(x_nodes, y_points)
f_interpolated_corrected = interpolator(m)

f_analytical = f(m)

results_corrected = {
    "Интерполированное значение m": f"{f_interpolated_corrected:.6f}",
    "Аналитическое значение m": f"{f_analytical:.6f}"
}

print(results_corrected)

