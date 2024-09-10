def armstrong(number, length_of_number, temp):
    sum = 0
    while (temp != 0):
        digit = temp % 10
        sum = sum + (digit ** length_of_number)
        temp = temp // 10
    if sum == number:
        return True
    else:
        return False


number = int(input("Enter a number: "))

length_of_number = len(str(number))

temp = number

result = armstrong(number, length_of_number, temp)

if result == True:
    print(f"{number} is Armstrong")
else:
    print(f"{number} is not Armstrong")