import sys
if __name__ == "__main__":
    line = input().strip()
    line = line[1:-1]
    array = list(map(int, line.split(',')))
    k = int(input().strip())
    newarray = []
    length = len(array)
    while length >= k:
        newarray += array[:k][::-1]
        array = array[k:]
        length = len(array)
    if array:
        newarray += array
    print('[',end = '')
    for i,v in enumerate(newarray):
        if i == len(newarray) - 1:
            print(v,end=']')
        else:
            print(v,end=',')
    print(newarray)
