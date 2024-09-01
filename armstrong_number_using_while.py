number = int(input("Enter a number: "))

digit_in_number = len(str(number))
sum = 0
temp = number

while (temp != 0):
    digit = temp%10
    sum = sum + (digit**digit_in_number)
    temp = temp//10

if sum == number:
    print(f"{number} is Armstrong")

else:
    print(f"{number} is not Armstrong")