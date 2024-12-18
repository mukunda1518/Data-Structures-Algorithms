# Problem : https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557



def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    
    def no_of_painters(boards, max_length):
        painters = 1
        units = 0
        for board in boards:
            if units + board > max_length:
                painters += 1
                units = board
            else:
                units += board
        return painters

    low, high = max(boards), sum(boards)

    while low <= high:
        mid = low + (high - low) // 2

        if no_of_painters(boards, mid) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low