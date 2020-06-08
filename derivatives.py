from sympy import symbols
from scipy.misc import derivative


# Using sympy to find the derivative of a function:
x, y, z = symbols("x y z")
equation = x ** 2 + 2 * x
deriv = equation.diff(x)
print(deriv)

# Using scipy.misc to find the derivative of a function at a point:
print(derivative(lambda x: x ** 2 + 2 * x, x0=1))

# Partial derivatives, sympy:
equation_2 = 2 * x * y ** 5 + 3 * x ** 2 * y + x ** 2
deriv_x = equation_2.diff(x)
deriv_y = equation_2.diff(y)
print(f"fx: {deriv_x}  fy: {deriv_y}")
