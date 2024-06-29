n = int(input())
A = n * []
A = list(map(int, input().split()))
B = n * [0]
for i in range(1, len(A), 2):
    B[i] = A[i-1]
    B[i-1] = A[i]
for j in range(0,len(B)):   
    print(B[j], end=" ")