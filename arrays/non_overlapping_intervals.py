# leetcode: https://leetcode.com/problems/non-overlapping-intervals/

if __name__ == "__main__":
    n = int(input())
    nums = [[int(i) for i in input().split()] for _ in range(n)]
    nums.sort(key=lambda x: [x[0], -x[1]])
    output = [nums[0]]
    for i in range(1, n):
        prev = output[-1]
        curr = nums[i]
        if prev[0] < curr[0] and prev[1] < curr[1]:
            output.append(curr)
        # if prev[1] < curr[1]:
        #     output.append(curr)
    print(len(output))
