def flattenNDList(data):
    flat = []
    for element in data:
        if type(element) == type([]):
            flat += flattenNDList(element) # recursively flattening the inner list
        else:
            flat += [element] # Append the elements in the list flat without using append()
    return flat

#labels = [['Electronics', ['Phones', 'Laptops']], ['Home Appliances', ['AC', 'TV']]]
labels = [['Stationary', 
           ['Pens', ['Ball pen', 'Roller pen', 'Fountain pen']], 
           ['Pencils', ['Wooden', 'Mechanical', 'Fansy']], 
           ['Bags', ['School', 'Laptop', 'Hand']]]]

print (f"The original list is: {labels}")
print (f"The flattened list is {flattenNDList(labels)}")