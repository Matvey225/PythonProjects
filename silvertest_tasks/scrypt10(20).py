def printHex(n):
    if n == 0:
        return
    else:
        printHex(n//16)
        print(n % 16, end='')
n = int(input())
printHex(n)