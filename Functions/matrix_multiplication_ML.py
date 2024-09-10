def matrix_multiplication(A,B):
    m = len(A) # rows in A
    n = len(A[0]) # columns in A which is same as the rows in B
    p = len(B[0]) # columns in B

    c = []
    # initializing the resulting matrix c with 0
    for i in range(m):
        c.append([0]*p)
    print(f"Resulting matrix just after initials")
    for i in c:
        print(i)
    
    # matrix multiplication step by step
    for i in range(m): #for each row in A
        for j in range(p): #for each column in B
            sum_value = 0
            for k in range(n): #multiply and sum up the row of A and column of B
                sum_value += A[i][k]*B[k][j]
            c[i][j] = sum_value #Store the result in c
    
    return c

A = [
    [1,2],
    [3,4]
]
B = [
    [5,6],
    [7,8]
]
C = matrix_multiplication(A,B)

print("Matrix A")
for row in A:
    print(row)

print("Matrix B")
for row in B:
    print(row)

print("The Resulting Matrix C:")
for row in C:
    print(row)


