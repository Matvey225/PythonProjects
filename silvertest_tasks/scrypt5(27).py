n = int(input())
A = list(map(int, input(). split()))
m = int(input())
B = list(map(int, input(). split()))
flag = True
for i in range(0, len(A)):
    for j in range(0, len(B)):
        if A[i] == B[j]:
            flag = False
    if flag == True:
        print(A[i], end=' ')
    flag = True