import numpy as np
from scipy.integrate import quad
from sympy import sin, cos
from math import pi


def f(t):
    """
    return (put the equation to integrate here.)
    """
    return (16 - 4 * cos(t) * 4 * sin(t)) * 4


t_low = 0  # Lower limit of integration
t_up = pi  # Upper limit of integration

integral = quad(f, t_low, t_up)

print("Result: {:.2f}".format(integral[0]))
print("Absolut error: {:.2f}%".format(integral[1]))
