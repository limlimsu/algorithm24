def multiply(A, B, C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

def print_matrix(M):
    for row in M:
        print(' '.join(map(str, row)))

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = [[0 for _ in range(len(A))] for _ in range(len(A))]

multiply(A, B, C)

print("Matrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)
print("\nMatrix C (Result of A * B):")
print_matrix(C)