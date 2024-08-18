n1, m1, value1 = [int(s) for s in input().split()]
def get_matrix(n, m, value):
    A = [0] * n
    for i in range(n):
        A[i] = [0] * m
        for j in range(m):
            A[i][j] = value
    return A
A1 = get_matrix(n1, m1, value1)
print(A1)
for i in range(n1):
    for j in range(m1):
        print(A1[i][j], end = " ")
    print(" ")
