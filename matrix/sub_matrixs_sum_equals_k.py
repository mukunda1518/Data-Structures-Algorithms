def sub_array_target_sum(row_sums, target):
    m = len(row_sums)
    count = 0
    for i in range(m):
        sum_ = 0
        for j in range(i, m):
            sum_ += row_sums[j]
            if sum_ == target:
                count += 1
    return count


def sub_matrix_target_sum(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    # Find the row prefix sum
    for i in range(m):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j - 1]

    count = 0
    for col1 in range(n):
        for col2 in range(col1, n):
            row_sums = [0] * m
            for k in range(m):
                if col1 == 0:
                    row_sums[k] = matrix[k][col2]
                else:
                    row_sums[k] = matrix[k][col2] - matrix[k][col1 - 1]
            count += sub_array_target_sum(row_sums, target)
    return count


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(sub_matrix_target_sum(matrix, k))
