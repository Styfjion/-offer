import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    array = list(range(1,n+1))
    index = []
    res1 = [unit for unit in array if unit%2 == 1]
    res2 = [unit for unit in array if unit%2 == 0]
    while res2:
        oldtop = res2.pop(0)
        res2.append(oldtop)
        index.append(res2.pop(0))
    result = res1+index
    for unit in result:
        print(unit,end=' ')