def get_permutations(up_word, p_word):
    if up_word == "":
        print(p_word)
        return
    char = up_word[0]
    for i in range(len(p_word)+1):
        new_p_word = p_word[0:i] + char + p_word[i:]
        get_permutations(up_word[1:], new_p_word)

def get_permutations_list(up_word, p_word):
    if up_word == "":
        return [p_word]
    char = up_word[0]
    all_permutations = []
    for i in range(len(p_word)+1):
        new_p_word = p_word[0:i] + char + p_word[i:]
        all_permutations.extend(get_permutations_list(up_word[1:], new_p_word))
    # print(all_permutations)
    return all_permutations


if __name__ == "__main__":
    # get_permutations("abc", "")
    print(get_permutations_list("abc", ""))


