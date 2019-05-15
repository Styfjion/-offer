class Tree:
    def __init__(x):
        self.var = x
        self.right = None
        self.left = None

def Solution(n,k):
    for i in range(1,k+1):
        if i == 1:
            node.append([1,-1])
        else:
            layer = []
            for j in range(2**(i-1),2**i):
                layer.append(j,-j)
            node.append(layer)
    for layer in node:




if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    Solution(n,k)

        