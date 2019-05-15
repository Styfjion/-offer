def solution(s):
    if not s:
        return ""
    num_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    dic = {")": "(", "]": "[", "}": "{"}
    while s[0] in dic.values():
        s = s[1:-1]
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] not in dic:
            stack.append(s[i])
        else:
            left = dic[s[i]]
            curs = ""
            while stack[-1] != left:
                curs += stack.pop()
            stack.pop()
            curnum = ""
            while stack and stack[-1] in num_set:
                curnum += stack.pop()
            curnum = int(curnum[::-1])
            curres = curs * curnum
            stack += curres.split()
    return "".join(stack[::-1])
 
s = input()
print(solution(s))