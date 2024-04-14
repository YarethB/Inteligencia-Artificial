import math
import random

def f(x):
    return x**4 + 3 * x**3 + 2 * x**2 - 1

def random_range(a, b):
    return a + random.random() * (b - a)

def simulated_annealing():
    T_inicial = 1000.0
    T_final = 0.1
    alfa = 0.95
    num_iteraciones = 10000

    x_actual = random_range(-10.0, 10.0)
    f_actual = f(x_actual)

    mejor_x = x_actual
    mejor_f = f_actual

    T = T_inicial

    for _ in range(num_iteraciones):
        x_vecino = x_actual + random_range(-0.1, 0.1)
        f_vecino = f(x_vecino)

        delta_E = f_vecino - f_actual

        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            x_actual = x_vecino
            f_actual = f_vecino

            if f_actual < mejor_f:
                mejor_x = x_actual
                mejor_f = f_actual

        T *= alfa
    return mejor_f, mejor_x


min_f, min_x = simulated_annealing()
print(f"Minimo valor de f(x) encontrado: {min_f:.4f} en x = {min_x: .4f}")
