# Memoization Method : Top - Down Approach
# get_nth_fibonacci_number_memoization
# Time Complexity - O(n)
# Space Complexity - O(n)

def get_nth_fib_num(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = get_nth_fib_num(n - 1, dp) + get_nth_fib_num(n - 2, dp)
    return dp[n]


# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n)
# Space Complexity - O(n)

def get_nth_fib_num1(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        num = dp[-1] + dp[-2]
        dp.append(num)
    return dp[-1]

# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(1)


def get_nth_fib_num2(n):
    if n <= 1:
        return n
    prev = 1
    prev2 = 0
    for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev


if __name__ == "__main__":
    n = int(input())
    dp = [-1] * (n + 1)
    print(get_nth_fib_num(n, dp))
    print(get_nth_fib_num1(n))
    print(get_nth_fib_num2(n))
