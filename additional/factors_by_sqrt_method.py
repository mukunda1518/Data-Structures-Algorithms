
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

def find_factors_of_number():
    n = 40
    i = 1
    while i * i <= n:
        if n % i == 0:
           print(i, n // i, end=" ") 
        i += 1

if __name__ == "__main__":
    find_factors_of_number()
