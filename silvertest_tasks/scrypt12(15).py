n = int(input())
max1 = 0
max2 = 0
num = n % 10
while n != 0:
    if  num > max1:
        max1 = num
    elif num < max1 and num > max2:
        max2 = num
    n //= 10
print(max1, max2)