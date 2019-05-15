def Test(matrix):
    print(matrix)
if __name__ == "__main__":
    yanglishu = int(input())
    result = []
    for i in range(yanglishu):
        n = int(input())
        matrix = []
        for j in range(n):
            matrix.append(list(map(int,input().split())))
        result.append(matrix)
    for unit in result:
        Test(unit)


