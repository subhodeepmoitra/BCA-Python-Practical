def getValue(nested_dict, keys):
    current_value = nested_dict
    for key in keys: # Traversing through each key in the list of keys
        current_value = current_value[key] # Updating the current value to be the value associated with the present key
    return current_value

def extractKeys(nested_dict):
    keys = []
    def traverse(d):
        for key, value in d.items(): #extracting the key-value pairs from the dictionary
            keys.append(key)
            if isinstance(value, dict):  # If the value is a nested dictionary, traverse it
                traverse(value)
    traverse(nested_dict)
    return keys

nested_dict = {'a': {'b': {'c': 1}}}
keys = extractKeys(nested_dict)

result = getValue(nested_dict, keys) # Access the nested value
print(f"The value inside the nested dictionary {nested_dict} is: {result}")  