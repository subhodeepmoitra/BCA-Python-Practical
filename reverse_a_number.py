number = int(input("Enter a number: "))

reverse = 0

while (number > 0):
    digit = number%10 #digit extraction
    reverse = reverse*10+digit
    number = number // 10
    print(f"Remaining digits: {number}")

print(f"{reverse} is the reversed number")
print(f"The original number now is {number}")