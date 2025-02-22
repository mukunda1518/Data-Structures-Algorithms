if __name__ == "__main__":
    path = input().split("/")
    stack = []
    for sub_path in path:
        if sub_path == "." or not sub_path:
            continue
        elif sub_path == "..":
            if stack:
                stack.pop()
        else:
            stack.append(sub_path)
            
    canonical_path = "/" + "/".join(stack)
    print(canonical_path)
 