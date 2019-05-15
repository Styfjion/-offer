

import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    m = a[0]
    n = a[1]
    result = []
    for i in range(m,n+1):
        if i == 370:
            a = 1
        target = i
        gewei = i%10
        i = int(i/10)
        shiwei = i%10
        i  = int(i/10)
        baiwei = i%10
        if gewei**3 + shiwei**3 + baiwei**3 == target:
            result.append(target)
    if not result:
        result = ['no']
    for unit in result:
        print(unit,end=' ')

    