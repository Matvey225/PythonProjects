N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N == M:
    if x < y:
        print(x)
    elif y < x:
        print(y)
    elif x == y:
        print(x)
elif x < y:
    if N < M:
        if x <= N - x:
            print(x)
        elif x >= N - x:
            print(N - x)
    elif M < N:
        if x <= M - x:
            print(x)
        elif x >= M - x:
            print(M - x)
elif y < x:
    if N > M:
        if y <= N - y:
            print(y)
        elif y >= N - y:
            print(N - y)
    elif M >= N:
        if y <= M - y:
            print(y)
        elif y >= M - y:
            print(M - y)
elif x == y:
    if N < M:
        if x <= N - x:
            print(x)
        elif x >= N - x:
            print(N - x)
    elif M > N:
        if x <= M - x:
            print(x)
        elif x >= M - x:
            print(M - x)