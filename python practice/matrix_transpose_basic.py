dimension = 4

def transpose(A, B):
    for rows in range(dimension):
        for columns in range(dimension):
            B[rows][columns] = A[columns][rows]


A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]
B = [[0]*dimension for _ in range(dimension)]

print("The original matrix is: ")
for i in range(dimension):
    for j in range(dimension):
        print(A[i][j], " ", end='')
    print() # New line

transpose(A, B)

print("The transposed matrix is: ")
for i in range(dimension):
    for j in range(dimension):
        print(B[i][j], " ", end='')
    print() # new line