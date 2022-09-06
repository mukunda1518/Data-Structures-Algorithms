def findnewfibseries(a, b, n):
    if n == 0:
        return a
    if n == 1:
        return b
    return findnewfibseries(a, b, n - 1) ^ findnewfibseries(a, b, n - 2)


t = int(input())

for i in range(0, t):
    nums = input()
    nums = nums.split(" ")
    nums = list(map(int, nums))
    a, b, n = nums[0], nums[1], nums[2]
    print(findnewfibseries(a, b, n % 3))
