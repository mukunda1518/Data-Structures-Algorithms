def get_flips(braces):
    if len(braces) % 2 == 1:
        return -1
    stack = []
    flips = 0
    for char in braces:
        if char == "}" and stack and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(char)
    open_braces = 0
    for char in stack:
        if char == "{":
            open_braces += 1 
    closed_braces = len(stack) - open_braces
    flips = (open_braces + 1) // 2 + (closed_braces + 1) // 2
    return flips

if __name__ == "__main__":
    braces = input()
    print(get_flips(braces))
    