n = int(input())

result = []

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        result.append("FizzBizz")
    elif i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(str(i))

#print(f"The resulting list is: {result}")
print(' '.join(result))