def sieve_of_eratosthenes(n):
    # Step 1: Create a list of boolean values, True means prime, False means not prime.
    primes = [True for i in range(n + 1)]
    p = 2  # The first prime number

    # Step 2: Starting from the first prime number, mark its multiples as non-prime.
    while p * p <= n:
        if primes[p]:  # If primes[p] is still True, it's a prime number
            # Marking multiples of p as False, starting from p*p
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1  # Move to the next number

    # Step 3: Collect all prime numbers
    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:  # If primes[p] is still True, it's a prime number
            prime_numbers.append(p)
    
    return prime_numbers

# Example usage:
n = 50  # Find prime numbers up to 50
prime_numbers = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n} are: {prime_numbers}")
