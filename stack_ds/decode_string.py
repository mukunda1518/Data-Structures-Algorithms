def get_decode_str_in_simple_way(s):
    stack = []
    curr_str = ""
    k = 0
    for char in s:
        if char == "[":
            stack.append((curr_str, k))
            curr_str = ""
            k = 0 
        elif char == "]":
            last_str, last_k = stack.pop()
            curr_str = last_str + curr_str * last_k
        elif char.isdigit():
            k = k * 10 + int(char)
        else:
            curr_str += char
    return curr_str

# Sample:
# input = x3[yz]
# output = xyzyzyz

if __name__ == "__main__":
    s = input()
    print(get_decode_str_in_simple_way(s))


