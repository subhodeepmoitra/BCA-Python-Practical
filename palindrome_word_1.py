text = input("Enter a number ")

text_lower = text.lower()

reverse = text_lower[::-1]
if text_lower == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


