import sys

if __name__ == "__main__":
    total = str(sys.stdin.readline().strip())
    target = str(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    layers = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        layer = list(map(int, line.split()))
        layers.append(layer)
    result = []
    for layer in layers:
        begin = layer[0]
        end = layer[1]
        qujian = total[begin-1:end]
        result.append(qujian.count(target))
    for item in result:
        print(item)