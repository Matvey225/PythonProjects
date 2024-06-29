m = int(input())
k = int(input())
s = int(input())
a = (k + s) % m == 0
print((k + s) % m + a * m)