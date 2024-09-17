mylist = [1,2,3,4,5,6,7,8,9,10]

""""
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

"""

"""
Using Lambda
"""

print(f"The original list is: {mylist}")

oddList = filter(lambda num: num % 2 != 0, mylist)
print(f"Dtype of odd list before casting: {type(oddList)}")
oddList = list(oddList)
print(f"Dtype of odd list after casting: {type(oddList)}")

evenList = filter(lambda num: num % 2 == 0, mylist)
print(f"Dtype of even list before casting: {type(evenList)}")
evenList = list(evenList)
print(f"Dtype of even list after casting: {type(evenList)}")

