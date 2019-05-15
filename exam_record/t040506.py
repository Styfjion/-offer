if __name__ == "__main__":
    N,K =map(int,input().strip().split())
    arrayList = []
    for i in range(N):
        arrayList.append(list(map(int,input().strip().split())))
    Dis = [0]*20000
    S = []
    res = []
    for i in arrayList:
        for j in range(arrayList[i][0],arrayList[i][1]+1):
            Dis[j] += 1
    i = 0
    while i<len(Dis):
        if Dis[i] >= K:
            j = i+1
            while j<len(Dis) and Dis[j] >= K:
                j += 1
            res.append([i,j-1])
            i=j
        else:
            i += 1
    print(len(res))
    for unit in res:
        print(unit[0],end=' ')
        print(unit[1])



    