import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    array = list(map(int, line.split()))
    value = []
    minindex = []
    for i in range(1,n):
        part = [abs(array[i]-array[j]) for j in range(i)]
        minv = min(part)
        value.append(minv)
        indexs = [index for index in range(i) if part[index] == minv]
        candidate = []
        for index in indexs:
            candidate.append(array[index])
        minindex.append(array.index(min(candidate))+1)
    for i in range(n-1):
        print(value[i],end=' ')
        print(minindex[i])



