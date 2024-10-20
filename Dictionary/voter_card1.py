def epicInsert(name, voter_id, voter_data):
    if voter_id in voter_data:
        print("Duplicate data not possible!")
    else:
        voter_data[voter_id] = name

def dataEntry():
    voter_data = {}
    while True:
        name = input("Enter voter's name (or type 'stop' to finish): ")
        if name.lower() == 'stop':  # Check for 'stop' to exit the loop
            break
        id = input("Enter card id: ")
        epicInsert(name, id, voter_data)  # Pass the voter_data dictionary
    return voter_data

data = dataEntry()
print(f"The data is: {data}")
