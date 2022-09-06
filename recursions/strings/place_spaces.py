def find_all_str(up_str, p_str):
    if len(up_str) == 1:
        return [p_str + up_str]
    arr = []
    arr.extend(find_all_str(up_str[1:], p_str + up_str[0] + " "))
    arr.extend(find_all_str(up_str[1:], p_str + up_str[0]))
    return arr
    
if __name__ == "__main__":
    print(sorted(find_all_str("ABCD", "")))
