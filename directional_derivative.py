"""
Calculate Directional derivative at a point
in the direction given by the unit vector.

"""
from sympy import lambdify, diff, symbols
import numpy as np


x, y, z = symbols("x y z")

point = (0, 1, 1)
vector = (0, 1, 1)
length_vector = (vector[0] + vector[1] + vector[2]) ** 0.5

unit_vector = (
    vector[0] / length_vector,
    vector[1] / length_vector,
    vector[2] / length_vector,
)


def function(x, y, z):
    return x ** 3 + y * z + 2 * x * z ** 2


deriv_x = lambdify((x, y, z), diff(function(x, y, z), x))
deriv_y = lambdify((x, y, z), diff(function(x, y, z), y))
deriv_z = lambdify((x, y, z), diff(function(x, y, z), z))

gradient_function = (
    deriv_x(point[0], point[1], point[2]),
    deriv_y(point[0], point[1], point[2]),
    deriv_z(point[0], point[1], point[2]),
)

v = np.array(unit_vector)
grad_f = np.array(gradient_function)
print(f" Directional derivative: {sum(v * grad_f)}")
