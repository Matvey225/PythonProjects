sum = 0
n = 1
flag = False
flag2 = False 
while n != 0 and flag != True and flag2 != True:
    n = int(input())
    sum += n
    if n == 0 and flag == False:
        flag = True
        continue 
    if flag == True and n == 0:
        flag2 == True
print(sum)