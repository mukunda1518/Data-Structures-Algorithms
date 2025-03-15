
# Problem: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

# https://www.youtube.com/watch?v=AsGzwR_FWok




class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        res, count = 0, 0
        i, j = 0, 0
        
        while i < len(arr):
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            res = max(count, res)
            
        return res