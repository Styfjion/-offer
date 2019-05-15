if __name__ == "__main__":
    count = int(input().strip())
    vistList = list(map(int,input().split()))
    sums1 = 0
    sums2 = 0
    sums3 = 0
    buy = 0
    sell = 0
    result =[]
    for i in range(count):
        result.append({'value':sums1,'buy':buy,'sell':sell})
        sum1 += vistList[0]
        buy += 1
        result.append({'value':sums2,'buy':buy,'sell':sell})
        sums3 -= vistList[0]
        sell += 1
        result.append({'value':sums3,'buy':buy,'sell':sell})


        