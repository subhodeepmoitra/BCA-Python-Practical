text = "Algorithm"
vowels= ['a', 'e', 'i', 'o', 'u']
container = []

for characters in text:
    print(characters)
    if characters == vowels:
        container.insert(characters)

print(f"The vowels in the string are: {container}")