# When the matrix is sorted totally

def binary_search(nums, row, l, r, target):
    while l <= r:
        mid = l + (r - l) // 2 
        if nums[row][mid] == target:
            return (row, mid)
        elif nums[row][mid] < target:
            l = mid + 1 
        else:
            r = mid - 1
    return (-1, -1)

def search_element_in_matrix(matrix, target):
    s_row = 0
    e_row = len(matrix) - 1 
    cols = len(matrix[0])
    
    # If matrix contains single row
    if e_row == 0:
        return binary_search(matrix, 0, 0, cols - 1, target)

    # Find the two rows
    m_col = cols // 2
    while s_row != e_row - 1:
        mid = s_row + (e_row - s_row) // 2
        if matrix[mid][m_col] == target:
            return (mid, m_col)
        elif matrix[mid][m_col] < target:
            s_row = mid 
        else:
            e_row = mid
    
    if matrix[s_row][m_col] == target:
        return (s_row, m_col)
    if matrix[e_row][m_col] == target:
        return (e_row, m_col)
    
    if matrix[s_row][m_col] > target:
        return binary_search(matrix, s_row, 0, m_col - 1, target)
    elif matrix[e_row][m_col] < target:
        return binary_search(matrix, e_row, m_col + 1, cols - 1, target)
    elif matrix[s_row][m_col] < target and matrix[s_row][cols-1] >= target:
        return binary_search(matrix, s_row, m_col + 1, cols - 1, target)
    else:
        return binary_search(matrix, e_row, 0, m_col - 1, target)


if __name__ == "__main__":
    matrix = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21],
        [22, 23, 24, 25]    
    ]
    target = 25 
    print(search_element_in_matrix(matrix, target))