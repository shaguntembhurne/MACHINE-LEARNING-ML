import numpy as np
print('THIS IS A MATRIX CAL HERE YOU ALL WILL SEE THE ADDITION, SUBSTRACTION, DETERMINANT OF THE MATRIX')

def getting_input():
    #HERE WE ARE GETTING THE INPUT FROM THE USER 
    row = int(input('Enter the number of rows: '))
    col = int(input('Enter the number of columns: '))

    print(f"ENTER ELEMENTS IN THE FORM OF {row}X{col} MATRIX")
    # THE MAIN STRUCTURE IS OVER HERE
    matrix = []
    for i in range(row):
        rows = list(map(int,input(f"enter row {i+1} (space seprated values): ").split()))
        matrix.append(rows)

    return np.array(matrix)


def main():
    #GET MATRIX FROM THE USER 
    print("Matrix A")
    A = getting_input()
    print('Matrix B')
    B = getting_input()

    if A.shape == B.shape:
        print("\n The addition for the matrix is\n",A+B)
        print("\n The multiplication for the matrix is\n",np.dot(A,B))
        print("\n The determinant will be\n",np.linalg.det(A))

    else:
        print("You have entered some wrong demensions of the matrix therefore it cant be computed")

if __name__ == "__main__":
    main()