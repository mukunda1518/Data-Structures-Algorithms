# Leetcode: https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        A_len, B_len = len(A), len(B)
        if A_len == 0:
            mid = B_len // 2
            if B_len % 2 == 1:
                return B[mid]
            else:
                return (B[mid - 1] + B[mid]) / 2
        total_len = A_len + B_len
        half = total_len // 2
        l, r = 0, A_len
        while True:
            i = l + (r - l) // 2  # index of A
            j = half - i - 2  # index of B
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < A_len else float("+inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < B_len else float("+inf")

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total_len % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


