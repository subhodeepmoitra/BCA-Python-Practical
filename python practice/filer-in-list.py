list = [1,2,3,4,5,6,7,8,9,10]

print(f"The original list is {list}")

odd = []
even = []

for num in list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Odd list {odd} and even list {even}")

print(f"Data type : {type(odd)}")

