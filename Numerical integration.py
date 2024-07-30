import numpy as np
def f(x):
    return x**2 + 5*x + 1
def trapezoidal(f, a, b):
    return (f(a) + f(b)) / 4 * (b - a)
def simpsons(f, a, b):
    h = (b - a) / 2
    return (f(a) + 4*f(a + h) + f(b)) * h / 3

a = 1
b = 8
integral_approx_trap = trapezoidal(f, a, b)
integral_approx_simp = simpsons(f, a, b)

print("Approximate integral (trapezoidal):", integral_approx_trap)
print("Approximate integral (Simpson's):", integral_approx_simp)
