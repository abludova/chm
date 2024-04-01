import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
def перваяСхема(a, rectangle):
    x, t, U = init(a, rectangle)
    I1 = I if rectangle else I + J
    for i in range(1, I1):
        for j in range(0, J):
            U[i][j + 1] = U[i - 1][j] + t_step * f(x[i], t[j])
    return U if rectangle else U[J:J + I + 1, :]

def втораяСхема(a, rectangle):
    x, t, U = init(a, rectangle)
    I1 = I if rectangle else I + J
    for i in range(I1 - 1, -1, -1):
        for j in range(0, J):
            U[i][j + 1] = U[i + 1][j] - t_step * f(x[i], t[j])
    return U if rectangle else U[0:I + 1, :]

def третьяСхема(a, rectangle):
    x, t, U = init(a, rectangle)
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i - 1][j + 1] + t_step * f(x[i], t[j])) / 2
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i + 1][j + 1] - t_step * f(x[i], t[j])) / 2
    return U

def четвертаяСхема(a, rectangle):
    x, t, U = init(a, rectangle)
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = U[i - 1][j] + t_step * f(x[i] + x_step / 2, t[j] + t_step / 2)
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = U[i + 1][j] - t_step * f(x[i] + x_step / 2, t[j] + t_step / 2)
    return U

def init(a, rectangle):
    ft = Ut_0 if a > 0 else Ut_1
    I1 = I if rectangle else I + J
    U = np.zeros((I1 + 1, J + 1))
    x = np.zeros(I1 + 1)
    t = np.zeros(J + 1)
    if rectangle:
        for i in range(I + 1):
            x[i] = x_step * i
            U[i][0] = Ux(x[i])
        if (a > 0):
            for j in range(J + 1):
                t[j] = t_step * j
                if (j != 0): U[0][j] = ft(t[j])
        else:
            for j in range(J + 1):
                t[j] = t_step * j
                if (j != 0): U[I][j] = ft(t[j])
    else:
        if (a > 0):
            for i in range(J + I + 1):
                x[i] = x_step * (i - J)
                U[i][0] = Ux(x[i])
        else:
            for i in range(I + J + 1):
                x[i] = i * x_step
                U[i][0] = Ux(x[i])
                for i in range(J + 1):
                    t[i] = i * t_step
    return x, t, U

def getSchemes(a, rectangle):
    if not rectangle and a > 0:
        return [(перваяСхема, f'Полуплоскость, a = {a}, схема 1')]
    if not rectangle and a < 0:
        return [(втораяСхема, f'Полуплоскость, a = {a}, схема 2')]
    if rectangle and a > 0:
        return [(перваяСхема, f'Прямоугольник, a = {a}, схема 1'), (третьяСхема, f'Прямоугольник, a = {a}, схема 3'), (четвертаяСхема, f'Прямоугольник, a = {a}, схема 4')]
    if rectangle and a < 0:
        return [(втораяСхема, f'Прямоугольник, a = {a}, схема 2'), (третьяСхема, f'Прямоугольник, a = {a}, схема 3'), (четвертаяСхема, f'Прямоугольник, a = {a}, схема 4')]

def solve(a, rectangle):
    return map(lambda scheme: (scheme[0](a, rectangle), scheme[1]), getSchemes(a, rectangle))

Ux = lambda x: 2 * x**2 + 4
Ut_0 = lambda t: 2*t**2 + 4
Ut_1 = lambda t: 2*t**2 + 6
f = lambda x, t: x
x_start, x_end = 0, 1
x_step = 0.1
t_start, t_end = 0, 10
t_step = 0.04
I = int((x_end - x_start) / x_step)
J = int((t_end - t_start) / t_step)

for (graph, title) in [*solve(-2, False), *solve(2, False), *solve(-2, True), *solve(2, True)]:
    x, t = np.linspace(x_start, x_end, I + 1), np.linspace(t_start, t_end, J + 1)
    print(title, 'x = ', x, 't = ', t, 'U = ', graph)
    x, t = np.meshgrid(x, t)
    x, t = x.T, t.T
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plt.title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("U")
    ax.set_rasterization_zorder(1)
    ax.plot_surface(x, t, graph, cmap=matplotlib.colormaps['jet'])
plt.show()
