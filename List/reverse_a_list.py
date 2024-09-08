def reverse_list(list, upper_bound):
    i=0
    while i < upper_bound//2:
        # Swapp elements from the start with the elements from the end iteratively
        list[i], list[upper_bound-i-1] = list[upper_bound-i-1], list[i]
        i += 1

    return list

list = []

upper_bound = int(input("Enter the upper-bound of the list: "))

for insert in range(0, upper_bound):
    element = int(input(f"Enter the element in place {insert+1}: "))
    list.append(element)

print(f"The original sequence is: {list}")
print(f"The return from reverse_list function is: {reverse_list(list, upper_bound)}")
