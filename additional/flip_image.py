# https://leetcode.com/problems/flipping-an-image/description/

if __name__ == "__main__":
    image = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    len_ = len(image[0])
    for row in image:
        i, j = 0, len_ - 1
        while i <= j:
            row[i], row[j] = row[j] ^ 1, row[i] ^ 1
            i += 1
            j -= 1
    print(image)