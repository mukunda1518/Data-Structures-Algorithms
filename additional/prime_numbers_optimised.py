


# Space complexity - O(n)
# Time complexity - O(n * log(log(n)))  = O(n) * n * (1/2 + 1/4 + 1/8 + ... + 1/n) = O(n) + log(log(n))
# Harmonic progression - n * (1/2 + 1/4 + 1/8 + ... + 1/n) = log(log(n))

def get_primes_upto_n():
    n = 40
    compose = [0] * (n + 1)
    i = 2
    while i * i <= n + 1:
        if not compose[i]:
            j = i * 2
            while j <= n:
                compose[j] = 1
                j += i
        i += 1
       
    print("Prime numbers")     
    for i in range(2, n + 1):
        if not compose[i]:
            print(i, end = ' ')


# Time complexixity is O(sqrt(n))
def is_prime_number(n):
    flag = True
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        i += 1
    if flag:
        print("{} is Prime".format(n))
    else:
        print("{} is not Prime".format(n))


if __name__ == "__main__":
    n = 36
    is_prime_number(n)
    get_primes_upto_n()
    