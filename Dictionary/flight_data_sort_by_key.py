def sortDictionary(data): #Bubble sort
    keys = list(data.keys())
    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]: #lexicographically comparing the keys similar to the way words are arranged in a dictionary
               keys[j], keys[j+1] = keys[j+1], keys[j]
    sorted_dictionary = {key: data[key] for key in keys}
    return sorted_dictionary

data = {
    "CVT001": {"source":"kolkata","destination":"delhi", "souls_on_board":125},
    "XVT002": {"source":"delhi","destination":"dubai", "souls_on_board":75},
    "AVT003": {"source":"jfk","destination":"madrid", "souls_on_board":265}
}

sorted_dict = sortDictionary(data)
print("Raw data", end="")
print()
for id, details in data.items():
    print(f"FID:{id}")
    for column, value in details.items():
        print(f"    {column}:{value}")
        
print("Sorted data", end="")
print()
for id, details in sorted_dict.items():
    print(f"FID:{id}")
    for column, value in details.items():
        print(f"    {column}:{value}")