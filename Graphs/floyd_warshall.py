# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

# https://www.youtube.com/watch?v=YbY8cVwWAvw


# Time Complexity - O(V^3)

class Solution:
    def shortest_distance(self, matrix):
        #Code here
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1e9
                if i == j:
                    matrix[i][j] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
            
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 1e9:
                        matrix[i][j] = -1
            
                    
