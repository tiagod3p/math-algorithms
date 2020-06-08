import numpy as np
from scipy.integrate import dblquad


def f(y, x):
    """
    return (put the equation to integrate here.)
    """
    return x ** 3


def y_low(x):
    """
    return (put the lower boundary curve here.)
    """
    return -(x ** 2) + 2


def y_up(x):
    """
    return (put the upper boundary curve here.)
    """
    return -(x ** 2) + 6


x_low = 1  # Lower limit of integration
x_up = 3  # Upper limit of integration

integral = dblquad(f, x_low, x_up, y_low, y_up)

print("Result: {:.2f}".format(integral[0]))
print("Absolut error: {:.2f}%".format(integral[1]))
