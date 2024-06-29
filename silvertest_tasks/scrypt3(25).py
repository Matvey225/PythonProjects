n = int(input())
a = [0] * 1000
count = 0
for i in range(100, 1000):
    if (i % 10) * (i // 10 % 10) * (i // 100) >= 100:
        a[i] = i
for i in a:
    if a[i] != 0 and count != n:
        print(a[i], '', end="")
        count += 1
