def add_edge(adj_list, vertex, dest):
    adj_list[vertex].append(dest)
    adj_list[dest].append(vertex)


def get_vertex(adj_list, n):
    maxi = len(adj_list[0])
    vertex = 0
    for i in range(1, n):
        if len(adj_list[i]) > maxi:
            maxi = len(adj_list[i])
            vertex = i
    return vertex


n = int(input())
adj_list = [[] for i in range(n + 1)]
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