def get_first_non_repeting_char_index(string):
    dict_s = {}
    for char in string:
        dict_s[char] = dict_s.get(char, 0) + 1 
    for key, val in dict_s.items():
        if val == 1:
            return string.index(key)
    return -1

if __name__ == "__main__":
    string = input()
    print(get_first_non_repeting_char_index(string))