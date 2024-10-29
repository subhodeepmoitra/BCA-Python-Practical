def invertDictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():  # Loop through the original dictionary and swap keys and values
        inverted_dict[value] = key
    return inverted_dict

original_dict = {'Amit': 19, 'Ravi': 20, 'Shukla': 30}
inverted_dict = invertDictionary(original_dict)
print(f"Original dictionary is: {original_dict}")  
print(f"Inverted dictionary is: {inverted_dict}")  
