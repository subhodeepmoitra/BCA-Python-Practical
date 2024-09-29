# Patient ID, Age, Gender, Tumor Size, Lymph Node Status, Histology Type(type of cancer cell), 
# Family History of Cancer, Cancer Diagnosis (0 for No, 1 for Yes)"""
# This code will remove the rows (datapoints) with null
data = [
    [1, 45, 'M', 2.5, 1, 'Ductal', 0, 1],  # Has cancer
    [2, 50, 'F', None, 0, 'Lobular', 1, 1],  # Tumor size is None
    [3, 62, 'M', 3.0, 1, 'Ductal', 0, 0],  # Does not have cancer
    [4, 38, 'F', 1.5, None, 'Lobular', 1, None],  # Lymph Node status and diagnosis are None
    [5, 55, 'M', 4.0, 0, 'Ductal', 0, 1],  # Has cancer
    [6, 29, 'F', 2.1, 1, 'Lobular', None, 0],  # Family history is None
    [7, 75, 'M', 5.5, 1, 'Ductal', 1, 1],  # Has cancer
    [8, 40, 'F', 2.8, 0, 'Ductal', 0, 0]   # Does not have cancer
]

print("The original data is:")
for row in data:
    print(row)

cleaned_data = [rows for rows in data if None not in rows]

print("The cleaned dataset is:")
for row in cleaned_data:
    print(row)