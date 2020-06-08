import numpy as np

array_1 = np.array([[1, 2, 3, 4, 5], [1, 2, 4, 3, 5]])

# Shows the dimensions of the array, (rows, columns)
print(f"shape of: \n{array_1} \nis: {array_1.shape}\n")

# Create an array filled with 0 values with the specified shape.
array_2 = np.zeros((4, 4), dtype=int)

# Create an array filled with 1 values with the specified shape.
array_3 = np.ones((4, 4), dtype=int)

# Create a random array
random_array = np.random.randint(1, 10, (5, 3))

# For multiplication of arrays use the function dot:
a = np.array([[1, 2, 3], [2, 1, 2]])  # (2,3)
b = np.array([[1, 2], [2, 1], [5, 2]])  # (3,2)
mult = a.dot(b)
print(f"Multiplication of \n{a} and \n{b} \nis: \n{mult}")
