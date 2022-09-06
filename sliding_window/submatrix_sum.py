# https://www.geeksforgeeks.org/submatrix-sum-queries/

def print_matrix_sub_array_sum(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    # Sum the rows
    for i in range(m):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j-1]
    
    # Sum columns
    for i in range(1, m):
        for j in range(n):
            matrix[i][j] += matrix[i-1][j]
    
    ans = [[0 for _ in range(n)]for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            x = min(i+k, m-1)
            y = min(j+k, n-1)
            ans[i][j] = matrix[x][y]
            
            row_bound = i - k - 1 
            col_bound = j - k - 1 
            is_row_bound_valid = False
            is_col_bound_valid = False
            
            if row_bound >= 0:
                ans[i][j] -= matrix[row_bound][y]
                is_row_bound_valid = True
            if col_bound >= 0:
                ans[i][j] -= matrix[x][col_bound]
                is_col_bound_valid = True
            if is_row_bound_valid and is_col_bound_valid:
                ans[i][j] += matrix[row_bound][col_bound]
    for row in ans:
        print(*row)


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    print_matrix_sub_array_sum(matrix, k)