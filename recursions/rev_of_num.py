
def rev_of_num(n, c):
    if n % 10 == n:
        return n
    return (10**c) * (n % 10) + rev_of_num(n//10, c-1)

n = int(input())
c = len(str(n))
print(rev_of_num(n, c-1))