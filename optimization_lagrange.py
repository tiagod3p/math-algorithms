"""
Finding the local maxima and minima
of a function subject to equality constraints
using lagrange multipliers.

"""
import numpy as np
from scipy.optimize import minimize


def f_objective(x0):
    """Function created to return the function
       that will be minimized/maximized.

    Args:
        x0 (array): Values of x, y, z

    Returns:
        The function to be minimized/maximized
    """
    x = x0[0]
    y = x0[1]
    z = x0[2]
    return x * y * z


def f_constraint(x0):
    """Function created to return the function constraint

    Args:
        x0 (array): Values of x, y, z

    Returns:
        The function constraint
    """
    x = x0[0]
    y = x0[1]
    z = x0[2]
    return x * y + 2 * y * z + 2 * x * z - 5


def objective(x0):
    """maximize or minimize?

    Args:
        x0 (array): Values of x, y, z

    Returns:
        If you want to minimize the f_objective: return f_objective(x0)
        If you want to maximize the f_objective: return -f_objective(x0)
    """
    return -f_objective(x0)


x0 = np.ones(3)  # It's equivalent to the lambda of lagrange multiplication

cons = {"type": "eq", "fun": f_constraint}

solution = minimize(
    objective, x0, method="SLSQP", constraints=cons, options={"disp": True}
)

xyz_otimized = solution.x

x_otimized = xyz_otimized[0]
y_otimized = xyz_otimized[1]
z_otimized = xyz_otimized[2]

print(f"X max/min: {x_otimized:.5f}")
print(f"Y max/min: {y_otimized:.5f}")
print(f"Z max/min: {z_otimized:.5f}")
