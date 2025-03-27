def add_edge(adj_list, vertex, dest):
    adj_list[vertex][0].append(dest)
    adj_list[dest][1].append(vertex)


def get_vertex(adj_list, n):
    max_diff = len(adj_list[0][0]) - len(adj_list[0][1])
    vertex = 0
    for i in range(1, n):
        diff = len(adj_list[i][0]) - len(adj_list[i][1])
        if diff > max_diff:
            max_diff = diff
            vertex = i
    return vertex


def apporach2():
    n = int(input())
    outdegree = [0] * n
    indegree = [0] * n
    for i in range(n):
        list_ = [int(i) for i in input().split()]
        list_ = list_[1:-1]

        for j in list_:
            outdegree[i] += 1
            indegree[j] += 1
    maxi = outdegree[0] - indegree[0]
    vertex = 0
    for i in range(1, n):
        if outdegree[i] - indegree[i] > maxi:
            maxi = outdegree[i] - indegree[i]
            vertex = i
    return vertex


n = int(input())
adj_list = [[[], []] for i in range(n + 1)]
for _ in range(n):
    list_ = [int(i) for i in input().split()]
    vertex = list_[0]
    len_ = len(list_[1:])
    for i in range(1, len_):
        dest = list_[i]
        if dest == -1:
            break
        add_edge(adj_list, vertex, dest)

print(get_vertex(adj_list, n))