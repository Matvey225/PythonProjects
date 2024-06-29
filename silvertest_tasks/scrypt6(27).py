n = int(input())
A = list(map(int, input().split()))
k, m = map(int, input().split())
flag = False
for i in range(0, len(A)):
    if A[i] > 99 and A[i] % k == 0 and A[i] % m != 0 and A[i] < 1000:
        print(A[i], end="")
        flag = True
if flag == False:
    print('0')