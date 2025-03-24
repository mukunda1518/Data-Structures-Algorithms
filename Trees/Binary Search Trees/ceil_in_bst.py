# Problem - https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
# https://www.youtube.com/watch?v=KSsk8AhdOZA&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=41



class Solution:
    def findCeil(self,root, inp):
        # code here
        val = -1
        
        while root:
            if root.key == inp:
                val = root.key
                break
            if inp < root.key:
                val = root.key
                root = root.left
            else:
                root = root.right
        return val

