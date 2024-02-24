import math

# Определение функции и её производной
def f(x):
    return 2 * math.sin(3 * x) - 1.5 * x

def df(x):
    return 6 * math.cos(3 * x) - 1.5

# Метод Ньютона
def newton_method(x0, tol=1e-7, max_iter=100):
    print("\nМетод Ньютона:")
    for k in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        print(f"k={k + 1}, x={x1}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

# Метод хорд
def chord_method(x0, x1, tol=1e-7, max_iter=100):
    print("\nМетод хорд:")
    for k in range(max_iter):
        x2 = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        print(f"k={k + 1}, x={x2}")
        if abs(x2 - x0) < tol:
            break
        x0 = x2

# Метод секущих
def secant_method(x0, x1, tol=1e-7, max_iter=100):
    print("\nМетод секущих:")
    for k in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"k={k + 1}, x={x2}")
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2

# Конечноразностный метод Ньютона
def finite_difference_newton(x0, h=0.01, tol=1e-7, max_iter=100):
    print("\nКонечноразностный метод Ньютона:")
    for k in range(max_iter):
        df_approx = (f(x0 + h) - f(x0)) / h
        x1 = x0 - f(x0) / df_approx
        print(f"k={k + 1}, x={x1}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

# Метод Стефессона
def steffensen_method(x0, tol=1e-7, max_iter=100):
    print("\nМетод Стефессона:")
    for k in range(max_iter):
        f_x0 = f(x0)
        f_x0_f_x0 = f(x0 + f_x0)
        x1 = x0 - (f_x0 ** 2) / (f_x0_f_x0 - f_x0)
        print(f"k={k + 1}, x={x1}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

# Метод простых итераций с tau = -0.2
def simple_iteration_method(x0, tau=0.2, tol=1e-7, max_iter=100):
    print("\nМетод простых итераций:")
    for k in range(max_iter):
        x1 = x0 + tau * f(x0)
        print(f"k={k + 1}, x={x1}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

# Выполнение методов с начальными значениями
x0 = 0.95  # Универсальное начальное приближение для методов, где это применимо
x0_chord = 0.8
x1_chord = 1.1
x0_secant = 0.8
x1_secant = 1.1

newton_method(x0)
chord_method(x0_chord, x1_chord)
secant_method(x0_secant, x1_secant)
finite_difference_newton(x0)
steffensen_method(x0)
simple_iteration_method(x0)
