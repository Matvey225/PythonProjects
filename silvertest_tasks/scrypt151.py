n = int(input())
s = 0
for i in range (1, n+1):
    s += i * (i - 1)
for j in range (1, n):
    print(j, "*", j+1, sep="", end="")
    if j != n - 1:
        print("+", end="")
print("=", s, sep="")