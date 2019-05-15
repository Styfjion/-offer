if __name__ == "__main__":
    n = int(input())
    if n < 6:
        print(0)
    else:
        print(2**(n-6)%666666666)