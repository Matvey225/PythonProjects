a, b, n = map(int, input(). split())
r = a * n
k = b * n
if k > 100:
    add = k // 100
    r = r + add
    k = k % 100
t1 = "rub. "
t2 = "kop."
print(r, t1, k, t2, sep="")