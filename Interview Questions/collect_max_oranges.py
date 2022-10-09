# User function Template for python3
from typing import List


class Solution:
    def collectMaximumOranges(self, trees, n, queries, q):
        trees.sort(key=lambda x: (x[0], x[1]))
        prefix_sum = [0] * (n + 1)
        positions = []
        for i, tup in enumerate(trees):
            prefix_sum[i + 1] = prefix_sum[i] + tup[1]
            positions.append(tup[0])
        answer = []
        for i in range(q):
            l, r = queries[i]
            k, m = 0, n - 1
            while k <= m:
                if positions[k] >= l and positions[m] <= r:
                    break
                if positions[k] < l:
                    k += 1
                if positions[m] > r:
                    m -= 1
            if k <= m:
                sum_ = prefix_sum[m + 1] - prefix_sum[k]
            else:
                sum_ = 0
            answer.append(sum_)

        return answer


# {
#  Driver Code Starts
# Initial Template for Python 3
from typing import List

if __name__ == "__main__":


    n, m = map(int, input().split())
    trees = [[0] * 2 for _ in range(n)]
    queries = [[0] * 2 for _ in range(m)]
    for i in range(n):
        a, b = map(int, input().split())
        trees[i][0] = a
        trees[i][1] = b

    for i in range(m):
        left, right = map(int, input().split())
        queries[i][0] = left
        queries[i][1] = right
    ob = Solution()
    ans = ob.collectMaximumOranges(trees, n, queries, m)
    for el in ans:
        print(el)

# } Driver Code Ends