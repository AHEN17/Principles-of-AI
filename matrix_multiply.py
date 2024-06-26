# Function to multiply two matrices
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrices dimensions incompatible for multiplication")
    
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Initialize result matrix with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Example usage:
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

print(matrix_multiply(matrix1, matrix2))  
# Output: [[58, 64], [139, 154]]
