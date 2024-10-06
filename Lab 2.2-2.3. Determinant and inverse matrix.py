def determinant_and_inverse(matrix):
    # Size of the matrix
    n = len(matrix)
    det = 1  # Initialize determinant

    # Create an augmented matrix (matrix | identity matrix)
    augmented_matrix = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform Gaussian elimination
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            # Swap with a row below if the pivot element is 0
            for k in range(i + 1, n):
                if augmented_matrix[k][i] != 0:
                    augmented_matrix[i], augmented_matrix[k] = augmented_matrix[k], augmented_matrix[i]
                    det *= -1  # Row swap changes determinant sign
                    break
            else:
                print("Matrix is singular and does not have an inverse.")
                return None, 0  # Singular matrix, determinant is 0

        # Get the pivot element
        pivot = augmented_matrix[i][i]
        det *= pivot  # Update determinant

        # Normalize the current row by the pivot element
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot

        # Eliminate the other rows
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix, det


# Example matrix
matrix = [
    [1, 4, 9],
    [3, 2, 7],
    [2, 1, 5]
]

# Calculate the inverse and determinant
inverse, det = determinant_and_inverse(matrix)

# Output results
print("Determinant:", det)
if inverse:
    print("Inverse matrix:")
    for row in inverse:
        print(row)
