n = int(input())
s = 1
for i in range(1, n+1):
    s *= (2 * i) / (2 * i + 1)
print(s)