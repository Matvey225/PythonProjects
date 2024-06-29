A = [0] * 25
small = 99
A = list(map(int, input(). split()))
for i in range(0, len(A)):
    if A[i] < small:
        small = A[i]
print(small)