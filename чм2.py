import numpy as np

# Метод Гаусса с выбором главного элемента
def gauss(A, b):
    n = len(A)
    for i in range(n):
        # Выбор главного элемента
        max_idx = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_idx]] = A[[max_idx, i]]
        b[[i, max_idx]] = b[[max_idx, i]]
        # Преобразование матрицы к треугольному виду
        for j in range(i+1, n):
            ratio = A[j, i] / A[i, i]
            A[j] -= ratio * A[i]
            b[j] -= ratio * b[i]
    
    # Вывод треугольного вида матрицы с заданной точностью
    print("Треугольный вид матрицы A:")
    for row in A:
        print(" ".join(f"{val:.10f}" for val in row))
    
    # Обратный ход
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    # Вывод решения
    print("\nРешение после обратного хода:")
    for xi in x:
        print(f"{xi:.10f}")

    # Погрешность
    error = np.linalg.norm(np.dot(A, x) - b)
    print("\nПогрешность:", error)
    return x

# Задаем данные
A = np.array([[2.12, 0.42, 1.34, 0.88],
              [0.42, 3.95, 1.87, 0.43],
              [1.34, 1.87, 2.98, 0.46],
              [0.88, 0.43, 0.46, 4.44]])
b = np.array([11.172, 0.115, 9.009, 9.349])

print("Метод Гаусса:")
gauss_result = gauss(A.copy(), b.copy())

# Метод Зейделя
def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = len(A)
    x = np.zeros(n)
    history = []  # Для хранения истории решений
    
    for iter in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x_old[i+1:])) / A[i, i]
        history.append(x.copy())
        if np.linalg.norm(x - x_old, np.inf) < tol:
            print("Решения последних трех итераций:", history[-3:])
            print("Общее количество итераций:", iter + 1)
            error = np.linalg.norm(b - np.dot(A, x))
            print("Погрешность:", error)
            return x
    raise Exception("Метод Зейделя не сошелся за максимальное число итераций.")

print("\nМетод Зейделя:")
try:
    gauss_seidel_result = gauss_seidel(A, b)
except Exception as e:
    print(e)
