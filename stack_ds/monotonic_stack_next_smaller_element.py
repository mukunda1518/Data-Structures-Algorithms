# https://www.interviewbit.com/problems/nearest-smaller-element/

# For Example

# Input 1:
#     A = [4, 5, 2, 10, 8]
# Output 1:
#     G = [-1, 4, -1, 2, 2]
# Explaination 1:
#     index 1: No element less than 4 in left of 4, G[1] = -1
#     index 2: A[1] is only element less than A[2], G[2] = A[1]
#     index 3: No element less than 2 in left of 2, G[3] = -1
#     index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
#     index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
    
# Input 2:
#     A = [3, 2, 1]
# Output 2:
#     [-1, -1, -1]
# Explaination 2:
#     index 1: No element less than 3 in left of 3, G[1] = -1
#     index 2: No element less than 2 in left of 2, G[2] = -1
#     index 3: No element less than 1 in left of 1, G[3] = -1




class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        n = len(A)
        G = [-1] * n
        
        for i in range(n):
            while stack and stack[-1] >= A[i]:
                stack.pop()
            if stack:
                G[i] = stack[-1]
            stack.append(A[i])
        return G