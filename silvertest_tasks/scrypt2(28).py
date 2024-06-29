n = int(input())
a, b = map(int, input().split())
A = n * [0]
A = list(map(int, input().split()))
B = n * [0]
for i, j in zip(range(len(A)), range(len(A) -1, -1, -1)):
    while i >= a-1 and i <= b-1:
        B[j] = A[i]
        break
    while i < a-1 or i > b-1:
        B[i] = A[i]
        break
for l in range(0, len(B)):
    print(B[l], end=' ')