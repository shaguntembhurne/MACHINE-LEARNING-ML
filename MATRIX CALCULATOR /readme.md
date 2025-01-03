
# Matrix Operations in Python

This Python program demonstrates basic matrix operations such as **addition**, **multiplication**, and **determinant** calculation using `numpy`. The user is prompted to input two matrices, and the program performs the operations if the matrices are compatible.

## Features

- **Matrix Addition**: Adds two matrices if they have the same dimensions.
- **Matrix Multiplication**: Multiplies two matrices using the dot product.
- **Determinant**: Calculates the determinant of a matrix.

## Requirements

- Python 3.x
- `numpy` library

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/matrix-operations.git
   ```

2. Install the required Python package:
   ```bash
   pip install numpy
   ```

## Usage

1. Run the program:
   ```bash
   python matrix_calculator.py
   ```

2. Follow the prompts to input two matrices. The program will:
   - Ask for the number of rows and columns for each matrix.
   - Prompt you to enter the matrix elements row by row.
   - Display the addition, multiplication, and determinant of the matrices (if the matrices are compatible).

## Code Explanation

### 1. **Getting Matrix Input**
   - The `getting_input()` function prompts the user to enter the dimensions and elements of a matrix.
   - It stores the matrix as a 2D list and converts it to a `numpy` array.

### 2. **Main Program Logic**
   - The `main()` function gets two matrices from the user.
   - It checks if the matrices have the same dimensions for addition and multiplication.
   - If the dimensions are compatible, it performs and prints the addition, multiplication, and determinant.
   - If the dimensions are not compatible, it shows an error message.

### 3. **Operations**
   - **Addition**: `A + B` adds two matrices element-wise.
   - **Multiplication**: `np.dot(A, B)` computes the dot product of two matrices.
   - **Determinant**: `np.linalg.det(A)` calculates the determinant of matrix `A`.

## Example Usage

```
Enter the number of rows: 2
Enter the number of columns: 2
ENTER ELEMENTS IN THE FORM OF 2X2 MATRIX
enter row 1 (space separated values): 1 2
enter row 2 (space separated values): 3 4
Matrix A
Matrix B
The addition for the matrix is
 [[ 2  4]
  [ 6  8]]

The multiplication for the matrix is
 [[ 7 10]
  [15 22]]

The determinant will be
 -2.0000000000000004
```

## Contribution

Feel free to fork the repository, modify the code, and create a pull request with improvements or new features!

