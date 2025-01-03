import numpy as np

# Creating Arrays
array1 = np.array([2, 3, 4])
array2 = np.zeros([2, 3])
array3 = np.ones([2, 3])
array4 = np.linspace(0, 10, 5)

# Printing created arrays
print(f"ONE SIMPLE ARRAY:\n{array1}")
print(f"ONE WITH ZEROS:\n{array2}")
print(f"ALL WITH ONES:\n{array3}")
print(f"LINSPACE (START, STEP, STOP):\n{array4}\n")

# Array Operations
array5 = np.array([2, 3, 4])
array6 = np.array([5, 6, 7])

sum_array = array5 + array6
mul_array = array5 * array6
scalar_array = array6 * 2
print(f"Sum of arrays: {sum_array}")
print(f"Multiplication of arrays: {mul_array}")
print(f"Scalar multiplication: {scalar_array}\n")

# Indexing and Slicing
array7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic slicing
print(f"Element at [1, 2]: {array7[1, 2]}")

# Slicing
print(f"Sliced array (first row):\n{array7[:1]}")

# Boolean Indexing
print(f"Elements > 5: {array7[array7 > 5]}\n")

# Aggregation and Mathematical Operations
# Aggregate operations
print(f"Sum of the array: {np.sum(array7)}")
print(f"Mean of the array: {np.mean(array7)}")
print(f"Max of the array: {np.max(array7)}")

# Sum along columns (axis=0) and rows (axis=1)
print(f"Sum along columns (axis=0): {np.sum(array7, axis=0)}")
print(f"Sum along rows (axis=1): {np.sum(array7, axis=1)}\n")

# Linear Algebra: Dot product
matrix_a = np.array([[1, 2], [2, 3]])
matrix_b = np.array([[4, 5], [6, 7]])
dot_product = np.dot(matrix_b, matrix_a)
print(f"The dot product of matrix_b and matrix_a is:\n{dot_product}\n")

# Random numbers
random_array = np.random.rand(2, 3)
random_int_array = np.random.randint(2, 3, (2, 2))
print(f"For the random array we have the output:\n{random_array}")
print(f"And if we specifically want the integers:\n{random_int_array}")
