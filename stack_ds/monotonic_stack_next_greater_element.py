# Leetcode: https://leetcode.com/problems/next-greater-element-i/description/

# Problem : https://www.youtube.com/watch?v=e7XQLtOQM3I


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge_map = {}
        stack = []
        len_ = len(nums2)

        for i in range(len_ - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                nge_map[nums2[i]] = -1
            else:
                nge_map[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(nge_map[num])
        return ans

