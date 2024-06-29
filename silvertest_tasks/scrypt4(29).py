n, a, b, c, d = map(int, input().split())
A = [i for i in range(1, n+1)]
B = []
C = []
for i in range(n):
    if i+1 != a:
        B.append(A[i])
    elif i+1 == a:
        for j in range((b-1), (a-2), -1):
            B.append(A[j])
        for j in range(b, n):
            B.append(A[j])
        break
    
for i in range(n):
    if i+1 != c:
        C.append(B[i])
    elif i+1 == c:
        for j in range((d-1), (c-2), -1):
            C.append(B[j])
        for j in range(d, n):
            C.append(B[j])
        break

print(*C)