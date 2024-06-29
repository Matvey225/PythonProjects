n = int(input())
A = n * []
A = list(map(int, input().split()))
score = 0
flag = False
for i in range(0, n):
    for j in range(i, n):
        if A[i] == A[j]:
            score += 1
    if score > 1:
        print(A[i], end=' ')
        flag = True
    score = 0
if flag == False:
    print('0')