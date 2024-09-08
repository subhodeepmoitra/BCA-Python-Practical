list = []

n = int(input("Enter the upper-bound of the list: "))

for i in range(0,n):
    element = int(input(f"Enter element in place {i+1}: "))
    list.append(element)

print(f"The formed list is: {list}")

# Finding max and min element in the list
min, max = list[0], list[0]

for i in range(1, n):
    if list[i] < min:
        min = list[i]

    if list[i] > max:
        max = list[i]

print(f"The max element is {max} and the min element is {min}")