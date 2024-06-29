def allNumBefN(n):
    print(n, "", end="")
    if n > 1:
        allNumBefN(n - 1)
n = int(input())
allNumBefN(n)