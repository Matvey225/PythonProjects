n = int(input())
n1 = n
an = 0
while n != 0:
    an = an * 10 + n % 10
    n = n // 10
print(an)
print(n1 - an)