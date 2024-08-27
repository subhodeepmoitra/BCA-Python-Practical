numbers = [1, 4, 9,16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter a number: "))

index = 0

while index < len(numbers):
    if (numbers[index] == x):
        print("Found at index: ", index+1)
    else:
        print("Searching...")
    index += 1

