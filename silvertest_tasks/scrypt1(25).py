n = int(input())
a = [0] * n
for i in range(n):
    if i == 0:
        a[i] = 1
    else:
        a[i] = a[i-1] * 2
for i in range(n):
    print(a[i], '', end="")