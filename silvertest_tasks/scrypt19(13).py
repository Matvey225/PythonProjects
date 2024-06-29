n = int(input())
big = 0
while n != 0:
    m = int(input())
    if m > n and m != 0:
        big += 1
    n = m
print(big)