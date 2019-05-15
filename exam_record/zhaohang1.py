import math
def solution2():
    n = int(input())
    m = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    print(max(max(l),math.ceil((sum(l)+m)/n)) ,max(l)+m)




if __name__ == "__main__":
    bandeng = int(input().strip())
    newpeople = int(input().strip())
    numberList = []
    for i in range(bandeng):
        numberList.append(int(input().strip()))
    maxN = max(numberList)+newpeople
    if bandeng > newpeople:
        minNumber = max(numberList)
    numberList.sort()
    maxNumber = max(numberList)
    token = True
    while newpeople and token:
        for i in range(bandeng-1):
            if numberList[i] == maxNumber:
                token  = False
                break
            newpeople -= (maxNumber-numberList[i])
            numberList[i] = maxNumber
            if not newpeople:
                minNumber = max(numberList)
                break
        break
    if not newpeople:
        minNumber = max(numberList)
    else:
        while newpeople:
            for i in range(bandeng):
                numberList[i] += 1
                newpeople -= 1
                if not newpeople:
                    break
    minNumber = max(numberList)
    print(minNumber,end=' ')
    print(maxN)
    
