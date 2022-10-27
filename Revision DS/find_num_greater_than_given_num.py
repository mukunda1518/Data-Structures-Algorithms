# Leetcode: https://leetcode.com/problems/next-greater-element-iii/description/


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        str_num = str(n)
        len_ = len(str_num)
        l = r = len_ - 1
        while l > 0:
            if int(str_num[l]) > int(str_num[l-1]):
                while True:
                    if int(str_num[r]) > int(str_num[l-1]):
                        break
                    r -= 1
                updated_str = str_num[0:l-1] + str_num[r] + str_num[l:r] + str_num[l-1] + str_num[r+1:]
                updated_str = updated_str[0:l] + updated_str[l:][::-1]
                if int(updated_str) > 2147483647:
                    return -1
                return updated_str
            l -= 1
        return -1



def get_permutations_list(up_word, p_word):
    if up_word == "":
        return [p_word]
    char = up_word[0]
    all_permutations = []
    for i in range(len(p_word)+1):
        new_p_word = p_word[0:i] + char + p_word[i:]
        all_permutations.extend(get_permutations_list(up_word[1:], new_p_word))
    return all_permutations


if __name__ == "__main__":
    num = input()
    per_nums = get_permutations_list(num, "")
    per_nums = [int(num) for num in per_nums]
    maxi = float("+inf")
    given_num = int(num)
    for num in per_nums:
        if num > given_num and num < maxi:
            maxi = num
    print(maxi)

