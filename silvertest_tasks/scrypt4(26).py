n = int(input())
A = [0] * n
boys = 0
girls = 0
countb = 0
countg = 0
A = list(map(int, input(). split()))
for i in range(0, len(A)):
    if A[i] < 0:
        boys += abs(A[i])
        countb += 1
    elif A[i] > 0:
        girls += A[i]
        countg += 1
avb = boys / countb
avg = (girls / countg) + 10
if avb >= avg:
    print("YES")
else:
    print("NO")