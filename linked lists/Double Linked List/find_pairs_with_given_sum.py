# Problem: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

from typing import Optional, List

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None


class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        temp = head
        tail = head
        while tail.next:
            tail = tail.next
        pairs = []
        while temp.data < tail.data:
            sum_ = temp.data + tail.data
            if sum_ == target:
                pairs.append((temp.data, tail.data))
                temp = temp.next
                tail = tail.prev
            elif sum_ < target:
                temp = temp.next
            else:
                tail = tail.prev
        
        return pairs