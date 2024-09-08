list = []

n = int(input("Enter the upper-bound of the list: "))

sum = 0

for i in range(0,n):
    element = int(input(f"Enter element {i+1}th: "))
    list.append(element)

print(f"The list is: {list}")

# Finding the sum of the elements in the list

for ele in range(0,n):
    sum = sum+list[ele]

print(f"The sum of the elements of the list is: {sum}")
