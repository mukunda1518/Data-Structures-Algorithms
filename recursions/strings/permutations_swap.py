def swap(s, index, i):
    temp = s[index]
    s[index] = s[i]
    s[i] = temp


def helper(s, index):
    if index == len(s) - 1:
        print(s)
        return
    for i in range(index, len(s)):
        s[i], s[index] = s[index], s[i]
        helper(s, index + 1)
        s[i], s[index] = s[index], s[i]


if __name__ == "__main__":
    s = "abc"
    helper(list(s), 0)

#
# # Function to swap two characters in a character array
# def swap(ch, i, j):
#     temp = ch[i]
#     ch[i] = ch[j]
#     ch[j] = temp
#
#
# # Recursive function to generate all permutations of a string
# def permutations(ch, curr_index=0):
#     if curr_index == len(ch) - 1:
#         print(''.join(ch))
#
#     for i in range(curr_index, len(ch)):
#         swap(ch, curr_index, i)
#         permutations(ch, curr_index + 1)
#         swap(ch, curr_index, i)
#
#
# if __name__ == '__main__':
#     s = 'ABC'
#     permutations(list(s))