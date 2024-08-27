num = int(input("Enter a number "))

reverse = int(str(num)[::-1])
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

'''
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/Palindrome_string_slicing_!.py"
Enter a number 121
Palindrome
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/Palindrome_string_slicing_!.py"
Enter a number 123
Not Palindrome
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/Palindrome_string_slicing_!.py"
Enter a number 123321
Palindrome
PS C:\Users\Subhodeep\Documents\BCA Python Practical> & C:/Users/Subhodeep/Documents/Python3.9.0/python.exe "c:/Users/Subhodeep/Documents/BCA Python Practical/Palindrome_string_slicing_!.py"
Enter a number 123322
Not Palindrome

'''