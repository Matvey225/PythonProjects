n = int(input())
answer = 1
flag = False
while n != 0: 
    if n > 13:
        answer *= (n % 10)
        flag = True
    n = int(input())
if flag == True:
    print(answer)
elif flag == False:
    print(0)