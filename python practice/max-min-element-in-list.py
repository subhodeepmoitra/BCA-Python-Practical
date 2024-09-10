def listMax(list, sizeList):
    max = list[0]

    for i in range(1, sizeList):
        if list[i] > max:
            max = list[i]
    return max

def listMin(list, sizeList):
    min = list[0]

    for i in range(1, sizeList):
        if list[i] < min:
            min = list[i]
    return min


list = []

sizeList = int(input("Enter the size of the list: "))

for insert in range(0, sizeList):
    element = int(input(f"Insert element in position {insert}: "))
    list.append(element)

max = listMax(list, sizeList)
min = listMin(list, sizeList)

print(f"In list {list} max is {max} and min is {min}")