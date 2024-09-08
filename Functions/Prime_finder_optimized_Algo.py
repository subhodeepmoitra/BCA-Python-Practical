def sieve(n):
    primes = [True for i in range(n+1)]
    p=2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i]=False
        p += 1

    
    prime_numbers_final_list = []
    for p in range (2,n+1):
        if primes[p]:
            prime_numbers_final_list.append(p)
    
    return prime_numbers_final_list



n=int(input("Enter the upper bound: "))

prime = sieve(n)
print(f"The list of prime numbers are: {prime}")
