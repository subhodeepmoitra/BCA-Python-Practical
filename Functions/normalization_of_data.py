# sensorData1, sensorData2, sensorData3
# 115, 126, 500
# 254, 189, 1500
# 2256, 11548, 205
# 14, 125, 4588



data = [
    [115, 126, 500],
    [254, 189, 1500],
    [2256, 11548, 205],
    [14, 125, 4588]
]

print(f"{'sensorData1':<12}{'sensorData2':<12}{'sensorData3':<12}")
for row in data:
    print(f"{row[0]:<12}{row[1]:<12}{row[2]:<12}")