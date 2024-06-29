a = int(input())
e = a % 10
d = a // 10 % 10
s = a // 100 % 10
t = a // 1000 % 10
dt = a // 10000
end = e**2 + d**2 + s**2 + t**2 + dt**2
print(end)