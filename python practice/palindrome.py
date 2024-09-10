def palindrome(number, temp):
    reverse = 0
    while(number > 0):
        digit = number % 10
        reverse = reverse*10+digit
        number = number // 10
    if reverse == temp:
        return True
    else:
        return False



number = int(input("Enter a number: "))
temp = number
result = palindrome(number, temp)
if result == True:
    print("Palindrome")
else:
    print("Not Palindrome")
