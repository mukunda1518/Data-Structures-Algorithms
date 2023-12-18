# Find XOR of numbers in range a to b

def find_xor(n):
    # Gives the XOR of numbers in range 0 - n
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    elif n % 4 == 3:
        return 0

if __name__ == "__main__":
    a, b = 3, 9
    
    # xor(a - b) = xor(0 - b) ^ xor(0 - (a-1))

    print(find_xor(b) ^ find_xor(a - 1))

    # Only for check, will give the time limit error for larger numbers
    ans = 0
    for i in range(a, b + 1):
        ans ^= i
    print(ans)

    