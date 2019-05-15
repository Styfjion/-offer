import sys

if __name__ == "__main__":
    input = str(sys.stdin.readline().strip())
    inputList = [ch for ch in input]
    result = [input]
    for i in range(len(inputList)):
        inputList.append(inputList.pop(0))
        newstr = ''.join(inputList)
        if not newstr in result:
            result.append(newstr)
        else:
            break
    print(len(result))

    