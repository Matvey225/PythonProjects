def printOct(num):
    if num == 0:
        return
    else:
        printOct(num // 8)
        print(num % 8, end='')
n = int(input())
printOct(n) 