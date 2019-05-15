import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    length = a[0]
    number = a[1]
    line = sys.stdin.readline().strip()
    inputList = list(map(int, line.split()))
    for i in range(number):
        if not sum(inputList):
            print(inputList[0])
            continue
        temp = inputList[:]
        maxNumber = max(inputList)
        for j in range(len(temp)):
            if not temp[j]:
                temp[j] = maxNumber
        minNumber = min(temp)
        print(minNumber)
        inputList = [unit-minNumber for unit in inputList if unit]

        
        
