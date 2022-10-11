# Geeks for Geeks : https://www.geeksforgeeks.org/minimum-edges-required-to-make-a-directed-graph-strongly-connected/

if __name__ == "__main__":
    n, k = map(int, input().split())
    vertex_set = set()
    indegree = {}
    outdegree = {}
    for _ in range(k):
        v1, v2 = map(int, input().split())
        outdegree[v1] = outdegree.get(v1, 0) + 1
        indegree[v2] = indegree.get(v2, 0) + 1
    indegree_count = len(indegree)
    outdegree_count = len(outdegree)
    edges = max(n - indegree_count, n - outdegree_count )
    print(edges)