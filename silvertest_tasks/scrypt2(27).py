n = int(input())
A = [0] * n
A = list(map(int, input(). split()))
flag = True
flag2 = False
for i in range(1, len(A)):
    if A[i] > 0 and A[i-1] > 0:
        print("YES")
        flag2 = True
        break
    elif A[i] < 0 and A[i-1] < 0:
        print("YES")
        flag2 = True
        break
if flag2 == False:
    print("NO")