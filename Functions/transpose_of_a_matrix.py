n = 3

def transpose(A, B):
    for i in range(n):
        for j in range(n):
            B[i][j] = A[j][i]

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[0] * n for _ in range(n)] # to create a new matrix B with all elements initialized to 0

print("The original matrix is: ")
for i in range(n):
    for j in range(n):
        print(A[i][j], "", end = '')
    print()

transpose(A, B)

print("The resultant transposed matrix is: ")
for i in range(n):
    for j in range(n):
        print(B[i][j], "", end = '')
    print()