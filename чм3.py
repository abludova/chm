import math
from scipy.integrate import quad

# Определение функции под интегралом
def f(x):
    return math.atan(x)

# Метод левых прямоугольников
def left_endpoint_rule(a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))

# Метод правых прямоугольников
def right_endpoint_rule(a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(1, n + 1))

# Метод средних прямоугольников
def middle_endpoint_rule(a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))

# Метод трапеций
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    return h * (0.5 * f(a) + 0.5 * f(b) + sum(f(a + i * h) for i in range(1, n)))

# Метод Симпсона
def simpsons_rule(a, b, n):
    h = (b - a) / n
    return (h / 3) * (f(a) + 2 * sum(f(a + i * h) for i in range(2, n, 2)) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + f(b))

# Нахождение n для заданной погрешности
def find_n_for_tolerance(method, a, b, tol):
    n = 1
    while True:
        approx_value = method(a, b, n)
        error = abs((exact_value - approx_value) / exact_value)
        if error < tol:
            break
        n *= 2
    return n, approx_value, error

# Вычисление точного значения интеграла
a, b = 0, 1
tol = 1e-5
exact_value, _ = quad(f, a, b)

# Вычисление для каждого метода и вывод результатов
methods = [
    (left_endpoint_rule, "левых прямоугольников"),
    (right_endpoint_rule, "правых прямоугольников"),
    (middle_endpoint_rule, "средних прямоугольников"),
    (trapezoidal_rule, "трапеций"),
    (simpsons_rule, "Симпсона")
]

for method, method_name in methods:
    n, approx_value, error = find_n_for_tolerance(method, a, b, tol)
    print(f"Метод {method_name}")
    print(f"Итоговый n: {n}")
    print(f"Последний шаг: {(b - a) / n:.12f}")
    print(f"Ответ: {approx_value:.12f}")
    print(f"Относительная погрешность: {error:.12f}")
    print()
