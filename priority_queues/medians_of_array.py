from queue import PriorityQueue

small = PriorityQueue()
large = PriorityQueue()
itr = 0

def find_medium(nums, index):
    global itr
    
    while itr <= index:
        small.put(-1 * nums[itr])
        large.put(-1 * small.queue[0])
        small.get()
        if small.qsize() < large.qsize():
            small.put(-1 * large.queue[0])
            large.get()
        itr += 1 
    
    if small.qsize() > large.qsize():
        print("%.2f" % (-1 * small.queue[0]), end=" ")
    else:
        print("%.2f" % ( (-1 * (small.queue[0] - large.queue[0]) ) / 2 ), end= " ")

def solve_queries(nums, queries):
    for i in queries:
        find_medium(nums, i)

if __name__ == "__main__":
    m, q = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    solve_queries(nums, queries)
