n = int(input())
a = 10**n-1
b = 10**(n-1)-1
for i in range(a, b, -2):
    if i % 2 != 0:
        print(i, "", end="")