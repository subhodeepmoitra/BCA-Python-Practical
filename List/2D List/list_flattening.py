def flatteningLoop(nestedList):
    flat = [] 
    for rows in nestedList: # each row is a seperate sub-list of the main list nestedList
        for item in rows: # each item is the seperate item in the sub-lists
            flat.append(item)
    
    return flat

# Driver code
data = [[1, 2, 3],
        ['A', 'B', 'C'],
        ['Oppenheimer', 'Feynman', 'Vonn Neuman']]

print("The original data is:")
for rows in data:
    for items in rows:
        print(items, "", end="")
    print()

print(f"The flattened list is: {flatteningLoop(data)}")