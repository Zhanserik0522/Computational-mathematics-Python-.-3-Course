from lab2_gauss_method import gaussian_elimination


# Custom square root function using Newton's method
def custom_sqrt(x, tolerance=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    if x == 0:
        return 0
    guess = x
    while True:
        new_guess = 0.5 * (guess + x / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess


# Check if matrix is symmetric
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


# Cholesky decomposition to decompose A into L * L^T
def cholesky_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]  # Initialize an empty matrix for L

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # Diagonal elements
                sum_k = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = custom_sqrt(matrix[i][i] - sum_k)
            else:
                # Off-diagonal elements
                sum_k = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - sum_k) / L[j][j]

    return L


def forward_substitution(L, B):
    n = len(L)
    y = [0] * n

    for i in range(n):
        sum_k = sum(L[i][k] * y[k] for k in range(i))
        y[i] = (B[i] - sum_k) / L[i][i]

    return y


def backward_substitution(L, y):
    n = len(L)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        sum_k = sum(L[k][i] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - sum_k) / L[i][i]

    return x


def solve_using_cholesky(A, B):
    if not is_symmetric(A):
        raise ValueError("Matrix A is not symmetric")

    # Step 1: Perform Cholesky decomposition to get L
    L = cholesky_decomposition(A)

    # Step 2: Solve Ly = B (forward substitution)
    y = forward_substitution(L, B)

    # Step 3: Solve L^T x = y (backward substitution)
    x = backward_substitution(L, y)

    return x


A = [
    [25, 15, -5],
    [15, 18, 0],
    [-5, 0, 11]
]

B = [30, 18, 6]

cholesky_solution = solve_using_cholesky([row[:] for row in A], B[:])
print("Solution using Cholesky Decomposition:", cholesky_solution)
gaussian_solution = gaussian_elimination([row[:] for row in A], B[:])
print("Solution using Gaussian Elimination:", gaussian_solution)
