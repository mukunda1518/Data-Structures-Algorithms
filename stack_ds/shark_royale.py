if __name__ == "__main__":
    n = int(input())
    sharks = list(map(int, input().split()))
    stack = [sharks[0]]
    for i in range(1, n):
        while stack and sharks[i] < 0 and stack[-1] > 0:
            if stack[-1] < -sharks[i]:
                stack.pop()
                continue
            if stack[-1] == -sharks[i]:
                stack.pop()
            break
        else:
            stack.append(sharks[i])
        
    print(*stack[::-1]) if stack else print(0)


# Smaple input
# 4
# -20 30 -10
# Output: 30 -20