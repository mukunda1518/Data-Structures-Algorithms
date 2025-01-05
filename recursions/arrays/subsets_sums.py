# Problem: https://www.geeksforgeeks.org/problems/subset-sums2234/1

# Input: arr[] = [2, 3]
# Output: [0, 2, 3, 5]

# Explanation: 
#     When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2.
#     When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.


# Time Complexity: O(2^N)
# Space Complexity: O(2^N)

class Solution:
    
    def get_all_subset_sums(self, ind, sum_, n, arr, res):
        if ind == n:
            res.append(sum_)
            return
        self.get_all_subset_sums(ind + 1, sum_ + arr[ind], n, arr, res)
        self.get_all_subset_sums(ind + 1, sum_, n, arr, res)

    def subsetSums(self, arr: list[int], N: int) -> list[int]:
        res = []
        self.get_all_subset_sums(0, 0, N, arr, res)
        return res

