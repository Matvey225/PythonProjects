n = input()
max1 = 0
max2 = 0
buf = 0
prev = 0
flag1 = False
flag2 = True
for i in n:
    if prev != i and flag1 == True:
        flag2 = False 
    if int(i) > int(max1) and int(i) > int(max2):
        buf = max1
        max1 = i
        max2 = buf
    if int(i) < int(max1) and int(i) > int(max2):
        max2 = i 
    prev = i 
    flag1 = True 
if flag2 == True:
    print("NO")
elif flag2 == False:
    print(max1, max2)