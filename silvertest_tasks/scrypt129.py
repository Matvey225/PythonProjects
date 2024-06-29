a, b, c, d = map(int, input().split())
m = a
if b > m:
    m = b
if c > m:
    m = c
if d > m:
    m = d
print(m)