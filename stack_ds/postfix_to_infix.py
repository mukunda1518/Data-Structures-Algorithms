# Probelm - https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1
# Youtube: https://www.youtube.com/watch?v=4pIc9UBHJtk



class Solution:
    def postToInfix(self, postfix):
        stack = []
        for i in range(len(postfix)):
            if 'A' <= postfix[i] <= 'Z' or 'a' <= postfix[i] <= 'z' or '0' <= postfix[i] <= '9':
                stack.append(postfix[i])
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                exp = "(" + top2 + postfix[i] + top1 + ")"
                stack.append(exp)
        return stack[0]

