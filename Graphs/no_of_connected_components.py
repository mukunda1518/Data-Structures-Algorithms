
# Problem: https://neetcode.io/problems/count-connected-components

# https://www.youtube.com/watch?v=8f1XPm4WOUc&t=668s



class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        par = [i for i in range(n)]
        size = [1] * n

        def find_parent(n1):
            if n1 == par[n1]:
                return n1
            par[n1] = find_parent(n1)
            return par[n1]
        
        def union_by_size(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2:
                return 0

            if size[p1] < size[p2]:
                par[p1] = p2
                size[p2] += size[p1]
            else:
                par[p2] = p1
                size[p1] += size[p2]
            return 1

        for n1, n2 in edges:
            union_by_size(n1, n2)
        
        res = 0
        for i in range(n):
            if i == find_parent(i):
                res += 1
        return res



