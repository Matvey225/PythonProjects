def printDev():
    n = int(input())
    while n != 0:
        for i in range(1, n+1):
            if n % i == 0:
                print(i, " ", end="", sep="")
        print()
        n = int(input())
printDev()