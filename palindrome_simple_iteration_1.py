num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp>0:
    remainder = temp%10
    reverse = (reverse * 10) + remainder # The "**" operator is used for 'power of" and "*" is used for multiplication.
    temp = temp//10

if num == reverse:
    print(num, "is palindrome")
else:
    print(f"{num} is not palindrome")


'''
The modulo (%) is defined as a remainder value when two numbers are divided.
    x = 5/2 #2.5 
    y = 5//2 #2 

'''