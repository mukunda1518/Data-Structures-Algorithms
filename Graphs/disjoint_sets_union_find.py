
# Concept: https://leetcode.com/discuss/post/5387528/what-is-the-disjoint-set-data-structure-l9hc7/

# https://www.youtube.com/watch?v=aBxjDBC4M1U

class DisjointSet:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find_ultimate_parent(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u: int, v: int):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        
        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[v] = ulp_u
        else:
            self.parent[v] = ulp_u
            self.rank[ulp_u] += 1
    
    def union_by_size(self, u: int, v: int):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.union_by_rank(1, 2)
    ds.union_by_rank(2, 3)
    ds.union_by_rank(4, 5)
    ds.union_by_rank(6, 7)
    ds.union_by_rank(5, 6)
    # checking 3 and 7 have same ultimate parent
    if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
        print("Same Ultimate Parent")
    else:
        print("Different Ultimate Parent")
    ds.union_by_rank(3, 7)
    if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
        print("Same Ultimate Parent")
    else:
        print("Different Ultimate Parent")
    # ---------------------
    print("-------------- Using Union by Size --------------")
    ds = DisjointSet(7)
    ds.union_by_size(1, 2)
    ds.union_by_size(2, 3)
    ds.union_by_size(4, 5)
    ds.union_by_size(6, 7)
    ds.union_by_size(5, 6)
    # checking 3 and 7 have same ultimate parent
    if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
        print("Same Ultimate Parent")
    else:
        print("Different Ultimate Parent")
    ds.union_by_size(3, 7)
    if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
        print("Same Ultimate Parent")
    else:
        print("Different Ultimate Parent")
    
    
    