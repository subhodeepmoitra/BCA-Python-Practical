num = int(input("Enter a number: "))

order = len(str(num)) #finding the length/total characters in the number entered
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order # sum = sum + (digit ** order)
    temp //= 10 # temp = temp // 10

# dislay result
if num == sum:
    print(num, "is armstrong")

else:
    print(f"{num} is not armstrong")

'''
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/armstrong_number_1.py"
Enter a number: 134
134 is not armstrong
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/armstrong_number_1.py"
Enter a number: 1634
1634 is armstrong
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/armstrong_number_1.py"
Enter a number: 663
663 is not armstrong
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/armstrong_number_1.py"
Enter a number: 407
407 is armstrong

'''