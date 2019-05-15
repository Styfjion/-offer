import sys
def MakeSmin(a,b,length):
    if not length:
        return 0
    if length == 1:
        return a[0]*b[0]
    if length!=len(a) or len(a)!=len(b):
        return -1
    c = b.copy()
    d = a.copy()

    while length>1:
        length -= 1
        c_max = max(c)
        c_max_index = c.index(c_max)
        d_min = min(d)
        d_min_index = d.index(d_min)
        if d_min_index != c_max_index:
            a[d_min_index],a[c_max_index] = a[c_max_index],a[d_min_index]
            d[d_min_index],d[c_max_index] = d[c_max_index],d[d_min_index]
        c[c_max_index] = -1
        d[c_max_index] = 101

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    b = list(map(int, line.split()))
    MakeSmin(a,b,n)
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    print(sum)


    

    


