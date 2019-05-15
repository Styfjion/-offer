import sys

def MinAlpha(string):
    stringList = list(string)
    strcopy = stringList.copy()
    for i in range(len(stringList)):
        if strcopy.count(stringList[i]) > 1 and i < len(stringList) - 1:
            if stringList[i]>=stringList[i+1]:
                strcopy.remove(stringList[i])

    return strcopy[0]

            
            

if __name__ == "__main__":
    str = str(sys.stdin.readline().strip())
    print(MinAlpha(str.lower()))
    