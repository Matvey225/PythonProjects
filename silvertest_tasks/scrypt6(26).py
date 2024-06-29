n = int(input())
A = [0] * n
A = list(map(int, input(). split()))
young = 0
count = 0
for i in range(0, len(A)):
    if A[i] >= young:
        young = A[i]
        count = i +1
print(count)