"""
Divergence and rotational of a vectorial field
"""
from sympy import symbols

x, y, z = symbols("x y z")

vector = (x * y ** 2 * z ** 2, x ** 2 * y * z ** 2, x ** 2 * y ** 2 * z)
vx = vector[0]
vy = vector[1]
vz = vector[2]

rotational = (
    vz.diff(y) - vy.diff(z),
    vx.diff(z) - vz.diff(x),
    vy.diff(x) - vx.diff(y),
)

divergence = vx.diff(x) + vy.diff(y) + vz.diff(z)

print(f"Vector: {vector}")
if rotational == (0, 0, 0):
    print(f"\tRotational: null vector {rotational}")
else:
    print(f"\tRotational: {rotational}")

print(f"\tDivergence: {divergence}")
