n = int(input())
for i in range(1, n+1):
    x = int(input())
    if i == 1:
        m = x
    if x > m:
        m = x
print(m)