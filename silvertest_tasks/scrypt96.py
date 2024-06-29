n = int(input())
e = n % 10
d = n // 10 % 10
s = n // 100
new =(s * 100) + (e * 10) + d
print(e + d + s, new)