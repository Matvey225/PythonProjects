n = int(input())
a = [0] * n
A = list(map(int, input(). split()))
a, b = map(int, input(). split())
ans = 0
for i in range(0, len(A)):
    if A[i] % a == 0 or A[i] % b == 0:
        ans += A[i]
print(ans)