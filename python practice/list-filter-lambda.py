mylist = [1,2,3,4,5,6,7,8,9,10]

print(f"The original list is {mylist}")

even = filter(lambda num:num % 2 == 0, mylist)
print(f"Data type of even before typecast: {type(even)}")
even = list(even)
print(f"Data type of even after typecast: {type(even)}")

odd = filter(lambda num:num % 2 != 0, mylist)
print(f"Data type of odd before typecast: {type(odd)}")
odd = list(odd)
print(f"Data type of odd after typecast: {type(odd)}")

print(f"Odd {odd} and even {even}")