def get_subseq(string, curr_str):
    if string == "":
        print(curr_str)
        return
    get_subseq(string[1:], curr_str + string[0])
    get_subseq(string[1:], curr_str)

def get_subseq_list(string, curr_str):
    if string == "":
        return [curr_str]
    left = get_subseq_list(string[1:], curr_str + string[0])
    right =  get_subseq_list(string[1:], curr_str)
    return left + right


if __name__ == "__main__":
    string = "abc"
    get_subseq(string, "")
    print(sorted(get_subseq_list(string, ""), key=lambda x: len(x)))
