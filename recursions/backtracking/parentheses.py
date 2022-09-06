def helper(n, str, open, close):
    if open == n and close == n:
        print(str)
        return
    if open < n:
        helper(n, str + "(", open + 1, close)
    if close < open:
        helper(n, str + ")", open, close + 1)
    
if __name__ == "__main__":

    helper(3, "", 0, 0)
    