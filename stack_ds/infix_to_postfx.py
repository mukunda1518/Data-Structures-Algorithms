# Problem: https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

# https://www.youtube.com/watch?v=4pIc9UBHJtk



# Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.

# Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
# Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
# Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.


# Example

# Input: s = "a+b*(c^d-e)^(f+g*h)-i"
# Output: abcd^e-fgh*+^*+i-
# Explanation: After converting the infix expression into postfix expression, the resultant expression will be abcd^e-fgh*+^*+i-


class Solution:
    
    def priority(self, char):
        if char == "^":
            return 3
        elif char in ["*", "/"]:
            return 2
        elif char in ["+", "-"]:
            return 1
        else:
            return -1
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        ans = ""
        stack = []
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                ans += s[i]
            elif s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
            else:
                while stack and self.priority(s[i]) <= self.priority(stack[-1]):
                    ans += stack.pop()
                stack.append(s[i])
        
        while stack:
            ans += stack.pop()
        return ans