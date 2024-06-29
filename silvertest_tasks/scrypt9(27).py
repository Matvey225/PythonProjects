n = int(input())
A = n * []
A = list(map(int, input().split()))
prev = A[0]
score1 = 1
score2 = 1
for i in range(1, n):
    if A[i] == prev:
        score1 += 1
    elif A[i] != prev:
        score2 = score1
        score1 = 1
        prev = A[i]
if score1 < score2:
    prev = A[i - score1]
    print(prev, score2)
elif score1 > score2:
    print(prev, score1)
