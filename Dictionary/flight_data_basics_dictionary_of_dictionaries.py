"""
fid   source      destination     souls_on_board
001   kolkata     delhi            125
002   delhi       dubai            75
003   jfk         madrid           265
"""

data = {
    "VT001": {"source":"kolkata","destination":"delhi", "souls_on_board":125},
    "VT002": {"source":"delhi","destination":"dubai", "souls_on_board":75},
    "VT003": {"source":"jfk","destination":"madrid", "souls_on_board":265}
}

print(data)

# printing the data in proper way
for fid, details in data.items():
    print(f"FID:{fid}")
    for column, value in details.items():
        print(f"    {column}:{value}")