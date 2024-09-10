def reverseList(list):
    i = 0
    size = len(list)
    while (i < size//2):
        list[i], list[size - i - 1] = list[size - i - 1], list[i]
        i += 1
    return list


list = []
size = int(input("Enter the size of the list: "))

for insert in range(0, size):
    element = int(input(f"Enter the element at position {insert}: "))
    list.append(element)

print(f"The list in normal order is: {list}")
print(f"The list in reverse order is: {reverseList(list)}")