# Given an array of coins[] of size n and a target value sum, where coins[i] represent the coins of different denominations
# You have an infinite supply of each of the coins.
# The task is to find the minimum number of coins required to make the given value sum.
# If it’s not possible to make a change, return -1.

# Problem - https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/


def get_minimum_number_of_coins(coins, target):
    coins.sort(reverse=True)
    res = 0
    
    for coin in coins:
        
        if target == 0:
            break
        
        if target >= coin:
            res += target // coin
            target %= coin
    
    return res if target == 0 else -1


if __name__ == "__main__":
    coins = [1, 5, 6, 9]
    target = 11
    print(get_minimum_number_of_coins(coins, target))

