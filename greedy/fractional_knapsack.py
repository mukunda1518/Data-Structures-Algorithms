

# Probelm - https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
# https://www.youtube.com/watch?v=1ibsQrnuEEg




class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        n = len(val)
        
        items = [(val[i], wt[i], val[i] / wt[i]) for i in range(n)]
        
        items.sort(key=lambda item: item[2], reverse=True)
        
        res = 0.0
        for value, weight, ratio in items:
            if capacity >= weight:
                res += value
                capacity -= weight
            else:
                res += (capacity * ratio)
                break

        return round(res, 6)
            
   