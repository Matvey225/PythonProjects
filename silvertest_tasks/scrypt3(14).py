n = 1
max1 = 0
max2 = 0
flag = False
flag2 = False
while n != 0:
    n = int(input())
    if flag == False and n != 0:
        max1 = n
    if flag2 == True and n != 0:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    if flag == True and n < max1 and n != 0 and n > max2:
        max2 = n
        flag2 = True
    elif flag == True and n > max1 and n != 0:
        max2 = max1
        max1 = n
        flag2 = True
    flag = True
print(max2)