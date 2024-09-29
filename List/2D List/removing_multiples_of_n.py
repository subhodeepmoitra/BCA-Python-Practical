def removeMultiplesN(data, n):
    remove = []
    for elements in data:
        if elements % n != 0:
            remove.append(elements)
    return remove

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = 3
print(f"The original list is {data} and after removing the multiples of 3 it becomes: {removeMultiplesN(data, n)}")