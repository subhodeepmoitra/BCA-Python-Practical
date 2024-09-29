def removeNull(data):
    cleanedDf = []
    for item in data:
        if item is not None:
            cleanedDf.append(item)
    return cleanedDf

data = [1,None,2,3,None,4,None,5,None]
print(f"The original dataframe is: {data}")
print(f"The cleaned dataframe using removeNull() is: {removeNull(data)}")
print(f"The cleaned dataframe using list comprehension is: {[item for item in data if item is not None]}")