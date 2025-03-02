
# https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1

# Youtube - https://www.youtube.com/watch?v=4pIc9UBHJtk



class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = [] 
        for i in range(len(pre_exp) - 1, -1, -1):
            if 'A' <= pre_exp[i] <= 'Z' or 'a' <= pre_exp[i] <= 'z' or '0' <= pre_exp[i] <= '9':
                stack.append(pre_exp[i])
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                exp = "(" + top1 + pre_exp[i] + top2 + ")"
                stack.append(exp)
        return stack[0]
                
