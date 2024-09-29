def noEven(listData):
    noEven_list = []
    for item in listData:
        if item % 2 != 0:
            noEven_list.append(item)
        else:
            pass
    return noEven_list

def noOdd(listData):
    noOdd_list = []
    for item in listData:
        if item % 2 == 0:
            noOdd_list.append(item)
    return noOdd_list



data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

noEven_list = noEven(data)
noOdd_list = noOdd(data)

print(f"The original list is: {data}")
print(f"The list without even is: {noEven_list}")
print(f"The list without odd is: {noOdd_list}")