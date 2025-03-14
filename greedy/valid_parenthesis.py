# Leetcode:




# Recurssion, trying out all the posibilites
# Time Complexity - O(3^^n)
class Solution:

    def is_valid_string(self, s, index, count):
        if count < 0:
            return False
        if index == len(s):
            return count == 0

        if s[index] == "(":
            return self.is_valid_string(s, index + 1, count + 1)
        if s[index] == ")":
            return self.is_valid_string(s, index + 1, count - 1)
        
        return self.is_valid_string(s, index + 1, count - 1) or self.is_valid_string(s, index + 1, count) or self.is_valid_string(s, index + 1, count + 1)

    def checkValidString(self, s: str) -> bool:
        return self.is_valid_string(s, 0, 0)


# Using 2 stacks


# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_s = []
        star_s = []

        for i, c in enumerate(s):
            if c == "(":
                open_s.append(i)
            elif c == "*":
                star_s.append(i)
            else:
                if open_s:
                    open_s.pop()
                elif star_s:
                    star_s.pop()
                else:
                    return False

        while open_s and star_s:
            if open_s.pop() > star_s.pop():
                return False
        
        return not open_s
        

# Approach 3 - Using 2 counts
# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_c = 0
        max_c = 0

        for c in s:
            if c == "(":
                min_c += 1
                max_c += 1
            elif c == ")":
                min_c -= 1
                max_c -= 1
            else:
                min_c -= 1
                max_c += 1

            if min_c < 0:
                min_c = 0

            if max_c < 0:
                return False
        return min_c == 0
