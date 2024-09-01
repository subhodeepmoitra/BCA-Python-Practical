# Sum of the digits of a number

number = int(input("Enter a number: "))

sum = 0

while (number > 0):
    digit = number % 10
    sum = sum + digit
    number = number//10

print ("The sum of the digits is: ", sum)