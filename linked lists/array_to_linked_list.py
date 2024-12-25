class Solution:
    def constructLL(self, arr):
        head = Node(arr[0])
        mover = head
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        return head
        

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
        print("~")
