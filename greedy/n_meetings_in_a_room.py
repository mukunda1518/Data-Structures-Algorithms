# Problem: https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

# https://www.youtube.com/watch?v=mKfhTotEguk


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        arr = [(start[i], end[i]) for i in range(len(start))]
        arr.sort(key=lambda x: x[1])
        count = 1
        free_slot = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0] > free_slot:
                count += 1
                free_slot = arr[i][1]
        return count