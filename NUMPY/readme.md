

# NumPy Array Operations

This project demonstrates various array operations using the NumPy library in Python. It covers creating arrays, performing basic mathematical operations, indexing and slicing, as well as using aggregation and random number generation techniques.

## Features

- **Creating Arrays**: Learn how to create arrays using `np.array()`, `np.zeros()`, `np.ones()`, and `np.linspace()`.
- **Array Operations**: Perform arithmetic operations like addition, multiplication, and scalar multiplication.
- **Indexing and Slicing**: Extract specific elements and subarrays using indexing and slicing techniques.
- **Boolean Indexing**: Filter elements based on conditions.
- **Aggregation**: Calculate sum, mean, and max of arrays.
- **Matrix Operations**: Perform dot product operations on matrices.
- **Random Number Generation**: Generate random arrays using `np.random.rand()` and `np.random.randint()`.

## Requirements

- Python 3.x
- NumPy library

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/numpy-array-operations.git
   ```

2. Install the required Python package (NumPy):
   ```bash
   pip install numpy
   ```

## Usage

1. Navigate to the project directory and run the script:
   ```bash
   python numpy_operations.py
   ```

2. The script will execute various array operations and print the results in the terminal.

## Code Explanation

### 1. **Creating Arrays**
   - `np.array()`: Create a simple 1D array.
   - `np.zeros()`: Create a 2D array of zeros.
   - `np.ones()`: Create a 2D array of ones.
   - `np.linspace()`: Create an array of equally spaced numbers between two values.

### 2. **Array Operations**
   - Addition, multiplication, and scalar multiplication of arrays are demonstrated.

### 3. **Indexing and Slicing**
   - Accessing specific elements in an array using index positions.
   - Slicing arrays to extract rows or columns.
   - Boolean indexing to filter elements based on conditions.

### 4. **Aggregation**
   - `np.sum()`, `np.mean()`, and `np.max()` are used to calculate the sum, mean, and maximum value of arrays.
   - Sum along specific axes (columns or rows).

### 5. **Matrix Operations**
   - Dot product of two matrices using `np.dot()`.

### 6. **Random Number Generation**
   - Random floating-point numbers using `np.random.rand()`.
   - Random integers using `np.random.randint()`.

## Example Output

```bash
ONE SIMPLE ARRAY:
[2 3 4]
ONE WITH ZEROS:
[[0. 0. 0.]
 [0. 0. 0.]]
ALL WITH ONES:
[[1. 1. 1.]
 [1. 1. 1.]]
LINSPACE (START, STEP, STOP):
[ 0.   2.5  5.   7.5 10. ]

Sum of arrays: [ 7  9 11]
Multiplication of arrays: [10 18 28]
Scalar multiplication: [10 12 14]

Element at [1, 2]: 6
Sliced array (first row):
[[1 2 3]]
Elements > 5: [6 7 8 9]

Sum of the array: 45
Mean of the array: 5.0
Max of the array: 9
Sum along columns (axis=0): [12 15 18]
Sum along rows (axis=1): [ 6 15 24]

The dot product of matrix_b and matrix_a is:
[[16 19]
 [24 28]]

For the random array we have the output:
[[0.51459139 0.39879669 0.67547429]
 [0.2676758  0.43851357 0.67674562]]
And if we specifically want the integers:
[[2 2]
 [2 2]]
```
