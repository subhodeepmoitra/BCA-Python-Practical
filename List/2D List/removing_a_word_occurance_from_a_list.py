def removeNull(data):
    cleanedData = []
    for items in data:
        if items != "NULL":
            cleanedData.append(items)
    return cleanedData

def removeNull_using_remove_method(data):
    for items in data:
        if items == "NULL":
            data.remove(items)
    return data

data = ['Kol', 'Bkp', 'Srp', 'Hwh', 'NULL', 'Bdc', 'NULL', 'Spr', 'NULL', 'NULL', 'Stg']
cleaned_list = removeNull(data)

print(f"The original dataset is: {data}")
print(f"(Using list comprehension) The cleaned dataset is: {[items for items in data if items != 'NULL']}") # list comprehension
print(f"(Using removeNull) The cleaned dataset is: {cleaned_list}")
print(f"(Using removeNull_using_remove_method) The cleaned dataset is: {removeNull_using_remove_method(data)}")
