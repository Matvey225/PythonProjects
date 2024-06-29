n = int(input())
max1 = 0
max2 = 0
while n != 0:
    if  n % 10 > max1:
        max1 = n % 10
    elif n % 10 < max1 and n % 10 > max2:
        max2 = n % 10
    n = n // 10
print(max1, max2)