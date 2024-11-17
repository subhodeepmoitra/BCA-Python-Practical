def matrixMultiplication(a,b):
    rowsA=len(a)
    colsA=len(a[0])
    rowsB=len(b)
    colsB=len(b[0])
    #checking if the no of cols of a is equal to the no of rows in b
    if colsA != rowsB:
        raise ValueError("Dimensionality Mismatch")
    #initializing the result with 0
    result=[]
    for i in range(rowsA):#loop through rows of a
        result.append([])#creating a new nested list in result
        for j in range(colsB):#loop through cols of b
            result[i].append(0)#putting 0 in the result matrix
    #doing matrix multiplication
    for i in range(rowsA):#looping through the rows of a
        for j in range(colsB):#looping through the columns in b
            for k in range(colsA):#looping each element of rows of a and the cols of b
                result[i][j] += a[i][k] * b[k][j]
    return result
        

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[3,6,9,12,11],
     [15,18,21,24,11],
     [27,30,33,36,11],
     [11,11,11,11,11]]
print("A")
for i in a:
    print(i)
print("B")
for i in b:
    print(i)
print("Result")
result=matrixMultiplication(a,b)
for i in result:
    print(i)
