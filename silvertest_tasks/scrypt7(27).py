n = int(input())
A = list(map(int, input().split()))
flag = True
flag2 = False
for i in A:
    if i == 1:
        flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i, end=' ')
        flag2 = True
    flag = True
if flag2 == False:
    print('0')