import sys
def Sum(m,n):
    if n<0 or m<=0:
        return False
    sum = 0
    begin = n
    for i in range(m):
        sum += begin
        begin = begin**0.5
    return sum

if __name__ == "__main__":
    '''
    line = sys.stdin.readline().strip()
    result = []
    while line:
        a = list(map(int, line.split()))
        n = a[0]
        m = a[1]
        result.append(Sum(m,n))
        line = sys.stdin.readline().strip()
    for unit in result:
        print('%.2f'%unit)
    '''
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    n = a[0]
    m = a[1]
    print('%.2f'%Sum(m,n))


    

    


