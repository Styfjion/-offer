
def points(input1,input2):
    strinput = [str(i) for i in input2]
    s1 = ''.join(strinput)
    s2 = s1[::-1]
    length = len(s1)
    temp=[[0 for i in range(length+1)]  for j in range(length+1)]
    for i in range(length):
        for j in range(length):
            if s1[i]==s2[j]:
                temp[i+1][j+1]=temp[i][j]+1
            else:
                temp[i+1][j+1]=max(temp[i][j+1],temp[i+1][j])
    return (length-temp[length][length] + 1)
if __name__ == "__main__":
    print(points(5,[1,3,1,5,2,5,1]))