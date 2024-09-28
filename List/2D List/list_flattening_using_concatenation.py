def flattenConcat(data):
    flat = []

    for rows in data:
        flat += rows
    
    return flat


# Driver code
data = [[1, 2, 3],
        ['A', 'B', 'C'],
        ['x-ray', 'uv-ray', 'ir-ray']]

"""data = [[1,2,3,10],
        [4,5,6,40],
        [7,8,9,70],]"""

print("The original data is:")
for rows in data:
    for items in rows:
        print(items, "", end="")
    print()

print(f"The flattened list is: {flattenConcat(data)}")