n, z = map(int, input(). split())
answer = 1
flag = False
while n != 0:
    if (n % 10) % z == 0:
        answer *= (n % 10)
        flag = True
    n //= 10
if flag == True:
    print(answer)
elif flag == False:
    print(0)