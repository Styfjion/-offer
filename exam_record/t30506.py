if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    if(N > M):
        print()
    else:
        H = list(map(int, input().split()))
        H.sort()
        total = 0
        ans = []
        for i in range(N-1):
            total += (H[N-1] - H[i])
        ans.append(total)
        for i in range(N, M):
            ans.append(ans[-1] - (H[i-1] - H[i-N]) + (H[i] - H[i-1]) * (N - 1))
        print(min(ans))


'''
if __name__ == "__main__":
    input1 =list(map(int,input().strip().split()))
    layerList = list(map(int,input().strip().split()))
    layerList.sort(reverse=True)
    M = input1[0]
    N = input1[1]
    layerSet = {}
    for i in set(layerList):
        layerSet[i] = layerList.count(i)
    countList = list(layerSet.values())
    if N<=max(countList):
        print(0)
    else:
        resultList = []
        for key in list(set(layerList)):
            count = layerSet[key]
            result = 0
            for unit in layerList:
                if unit < key:
                    result += key - unit
                    count += 1
                    if count == N:
                        resultList.append(result)
                        break
        print(min(resultList))
'''
    
        
