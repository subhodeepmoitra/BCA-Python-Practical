# In ML numbers can be big and small, so to bring them all in a same scale (between 0 to 1) we use Normalization
# Normalization is also called Feature Scaling

def normalization(data):
    minData = min(data)
    maxdata = max(data)
    normalized = []

    #Normalizing each number using loop
    for x in data:
        normalized_data = (x-minData)/(maxdata-minData)
        normalized.append(normalized_data)

    return normalized

data = []
n = int(input("Enter the upper-bound of the list: "))

for insert in range(0,n):
    element = int(input(f"{insert+1} Insert data: "))
    data.append(element)

print(f"The original data: {data}")
normalizedData = normalization(data)
print(f"The normalized data: {normalizedData}")