n = int(input())
A = n * []
A = list(map(int, input().split()))
r = int(input())
B = n * [0]
print('before:', end=' ')
for i in range(0, len(A)):
    print(A[i], end=' ')
for i in range(0, len(A)):
    if (i + r) >= len(A):
        B[i+r-(len(B))] = A[i]
    elif (i + r) < len(A):
        B[i+r] = A[i]
print()
print('after:', end=' ')
for j in range(0, len(B)):
    print(B[j], end=' ')