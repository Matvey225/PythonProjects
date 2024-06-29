def printNtoP(N, P):
    if N == 0:
        return
    else:
        printNtoP(N // P, P)
        print(N % P, end='')
N, P = map(int, input(). split())
printNtoP(N, P)