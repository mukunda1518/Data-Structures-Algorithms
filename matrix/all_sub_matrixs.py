def ContinSubSeq(lst):
    size=len(lst)
    for start in range(size):
        for end in range(start+1,size+1):
            yield (start,end)


def getsubmat(mat,start_row,end_row,start_col,end_col):
    return [i[start_col:end_col] for i in mat[start_row:end_row] ]


def get_all_sub_mat(mat):
    rows = len(mat)
    cols = len(mat[0])
    for start_row, end_row in ContinSubSeq(list(range(rows))):
        for start_col, end_col in ContinSubSeq(list(range(cols))):
            yield getsubmat(mat,start_row,end_row,start_col,end_col)


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sub_matrixs = get_all_sub_mat(matrix)
    for each in sub_matrixs:
        for row in each:
            print(row)
        print()
