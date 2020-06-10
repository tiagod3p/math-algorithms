"""
Find the maximum rate of change of a function at a point
"""
from sympy import lambdify, diff, symbols
import numpy as np

x, y, z = symbols("x y z")

point = (1, -1, -1)


def function(x, y, z):
    return x * y ** 2 + x ** 2 * z + y * z ** 2


deriv_x = lambdify((x, y, z), diff(function(x, y, z), x))
deriv_y = lambdify((x, y, z), diff(function(x, y, z), y))
deriv_z = lambdify((x, y, z), diff(function(x, y, z), z))

gradient_f = (
    deriv_x(point[0], point[1], point[2]),
    deriv_y(point[0], point[1], point[2]),
    deriv_z(point[0], point[1], point[2]),
)

rate_max = (gradient_f[0] ** 2 + gradient_f[1] ** 2 + gradient_f[2] ** 2) ** 0.5
print(f"The maximum rate of change is: {rate_max:.3f}")
