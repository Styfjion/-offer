 
import numpy as np
if __name__ == "__main__":
    inputList = list(map(int,input().split()))
    rows = inputList[0]
    cols = inputList[1]
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int,input().split())))
    
    inputList2 = list(map(int,input().split()))
    posX = inputList2[:2]
    posY = inputList2[2:]
    matrixMark = np.zeros((row,cols)).tolist()
    def moving(fur,cur,rows,cols,matrix):
        


