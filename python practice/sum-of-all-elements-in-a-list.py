def sumofList(list, size_of_list):
    sum = 0
    for element in range(0, size_of_list):
        sum = sum + list[element]
    return sum



list = []

size_of_list = int(input("Enter the size of the list: "))

for inset in range(0, size_of_list):
    element = int(input(f"Enter element at position {inset}: "))
    list.append(element)

print(f"The created list is: {list}")

sum = sumofList(list, size_of_list)

print(f"The sum of the elements in list {list} is: {sum}")