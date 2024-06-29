n = 1
an = 0
big = 0
while n != 0:
    n = int(input())
    if n > big:
        big = n
        an = 1
    elif n == big:
        an += 1
print(an)