class Interval:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end 


def find_all_interval_intersections(a, b):
    a_len = len(a)
    b_len = len(b)
    i, j = 0, 0
    res = []
    while i < a_len and j < b_len:
        if a[i].start <= b[j].end and b[j].start <= a[i].end:
            res.append([max(a[i].start, b[j].start), min(a[i].end, b[j].end)])
        if a[i].end < b[j].end:
            i += 1 
        else:
            j += 1
    return res

if __name__ == "__main__":
    n = int(input())
    a, b = [], []
    a = [Interval(*[int(each) for each in input().split()]) for _ in range(n)]
    # for i in range(n):
    #     s, e = map(int, input().split())
    #     a.append(Interval(s, e))
    
    b = [Interval(*[int(each) for each in input().split()]) for _ in range(n)]
    # for i in range(n):
    #     s, e = map(int, input().split())
    #     b.append(Interval(s, e))
    
    intersections = find_all_interval_intersections(a, b)
    
    for each in intersections:
        print(*each)
    