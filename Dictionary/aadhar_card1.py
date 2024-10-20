aadhar_card = {}

while(-1):
    name = input("Enter the name of the contact: ")
    number = int(input("Aadhar number: "))
    if number in aadhar_card: #check if number is key in the aadhar_card?
        print("Duplicate aadhar not possible!")
    elif name == 'stop':
        break
    else:
        aadhar_card[number] = name
        
print(aadhar_card)