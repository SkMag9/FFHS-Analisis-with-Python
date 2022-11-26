#
#   Semesterarbeit AnPy - Abgabe 4
#   
#
import numpy as np
import sympy as sy
import scipy.integrate as integrate


def calc_func(f, x):
    x_s = sy.symbols("x")
    expr = sy.sympify(f)
    expr_sub = expr.subs(x_s, x)
    return expr_sub.evalf()


def calc_integral_diff(f, a, b, result):
    # Standardmässig liefert quad auch die erwartete Abweichung mit, mit [0] liefert es nur das Resultat.
    print("\tSciPi Integral: " + str(integrate.quad(f, a, b)[0]))
    return print("\tAbweichung: " + str(result - integrate.quad(f, a, b)[0]))


def sekanten_trapez(f, a, b, n):
    grenzen = np.linspace(a, b, n+1)
    result: int = 0
    for x in range(n):
        a = grenzen[x]
        b = grenzen[x + 1]
        result += ((b - a) / 2) * ((calc_func(f, a)) + (calc_func(f, b)))
    print("Sekantentrapez-Regel" + str(result))
    return result


def tangenten_trapez(f, a, b, n):
    grenzen = np.linspace(a, b, n+1)
    result: int = 0
    for x in range(n):
        a = grenzen[x]
        b = grenzen[x + 1]
        result += (b - a) * (calc_func(f, ((a + b)/2)))
    print("Tangententrapez-Regel: " + str(result))
    return result


def simpson(f, a, b, n):
    grenzen = np.linspace(a, b, n+1)
    result: int = 0
    for x in range(n):
        a = grenzen[x]
        b = grenzen[x+1]
        result += ((b - a)/6) * ((calc_func(f, a)) + (4 * calc_func(f, (a + b)/2)) + (calc_func(f, b)))
    print("Simpson Regel: " + str(result))
    return result


def main():
    calc_integral_diff(lambda x: (x-1), 0, 2, sekanten_trapez("x-1", 0, 2, anzahl))


if __name__ == '__main__':
    main()
