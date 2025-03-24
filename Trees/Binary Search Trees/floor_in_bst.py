# Problem: https://www.geeksforgeeks.org/problems/floor-in-bst/1
# https://www.youtube.com/watch?v=xm_W1ub-K-w&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=42



class Solution:
    def floor(self, root, x):
        # Code here
        val = -1
        while root:
            if root.data == x:
                val = root.data
                break
            elif root.data < x:
                val = root.data
                root = root.right
            else:
                root = root.left
        return val