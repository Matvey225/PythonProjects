A = list(map(int, input(). split()))
prev = 0
ans = 0
for i in range(0, len(A)):
    if A[i] != prev:
        ans += 1
        prev = A[i]
print(ans)