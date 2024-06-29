A = list(map(int, input().split()))
small = 21
big = 0
sum = 0
memo = 0
flag1 = False
flag2 = False
for i in A:
    if i < small:
        small = i
    elif i > big:
        big = i

for i in A:
    if i == small and flag1 == False:
        print('(', i, ')', sep='', end=' ')
        flag1 = True
    elif i != big:
        print(i, end=' ')
        sum += i
for i in range(len(A), -1, -1):
    if i == big and flag2 == False:
        print('(', i, ')', sep='', end=' ')
    
print('=', sum, sep=' ')