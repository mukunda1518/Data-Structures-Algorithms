def sieve(n, primes):
    i = 2
    while i * i <= n:
        if not primes[i]:
            j = i * 2 
            while j <= n:
                primes[j] = True
                j += i
        i += 1
    
    for i in range(2, n + 1):
        if not primes[i]:
            print(i, end=" ")

if __name__ == "__main__":
    n = 40
    primes = [0] * (n + 1)
    sieve(n, primes)

