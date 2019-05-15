if __name__ == "__main__":
    input1 =list(map(int,input().strip().split()))
    kindList = list(map(int,input().strip().split()))
    total = input1[0]
    kind = input1[1]
    result = sum(kindList)-(kind-1)*total
    if result > 0:
        print(result)
    else:
        print(0)
