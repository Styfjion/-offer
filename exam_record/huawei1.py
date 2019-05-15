if __name__ == "__main__":
    inputList = input().strip().split()
    number = int(inputList[0])
    strList = list(map(str,inputList[1:]))
    result = []
    for unit in strList:
        if len(unit) < 8:
            unit += '0'*(8-len(unit))
            result.append(unit)
        else:
            numEight = int(len(unit)/8)
            for i in range(1,numEight+1):
                result.append(unit[(i-1)*8:i*8])
            if len(unit) - 8*numEight:
                res = unit[8*numEight:] + '0'*((numEight+1)*8-len(unit))
                result.append(res)
    result.sort()
    result = ' '.join(result)
    print(result)

def solution2(s):
    res1 = s.split()[1:]
    res1 = [i for i in res1 if i]
    res2 = []
    for subs in res1:
        if len(subs) <= 8:
            res2.append(subs + "0"*(8-len(subs)))
        else:
            while len(subs) > 8:
                res2.append(subs[:8])
                subs = subs[8:]
            res2.append(subs + "0"*(8-len(subs)))
    res2.sort()
    return " ".join(res2)

        