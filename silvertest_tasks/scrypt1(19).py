def sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

max = 0
nmax = 0
for i in range(5): 
    n = int(input())
    if sum(n) > max:
        max = sum(n)
        nmax = n
    if n > nmax and max == sum(n):
        nmax = n
        max = sum(n)
print(nmax)