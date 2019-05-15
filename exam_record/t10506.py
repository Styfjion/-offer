if __name__ == "__main__":
    s = str(input().strip())
    stack = []
    count = 0
    while s:
        top = stack[-1] if stack else '#'
        if s[0] == top:
            stack.pop()
            count += 1
        else:
            stack.append(s[0])
        s = s[1:]
    print(count)

        