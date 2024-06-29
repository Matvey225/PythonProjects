a, b = map(int, input(). split())
s = 1
flag = False
for i in range(a, b+1):
    if (i * 6) % 10 == 2:
        s *= i
        flag = True
if flag == True:
    print(s)
if flag == False:
    s = 0
    print(s)