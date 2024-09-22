n = 100

def sieve(n):
    primes = [True for i in range(n+1)]
    p=2
    while p*p<=n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    
    prime_nos = []

    for p in range(2, n+1):
        if primes[p]:
            prime_nos.append(p)
    return prime_nos

prime = sieve(n)
print(f"The prime numbers between {n} are: {prime}")