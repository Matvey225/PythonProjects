n = int(input())
flag = False
while n != 0:
    first = n % 10
    second = n // 10 % 10
    if first == second:
        flag = True
        break
    n //= 10
if flag == True:
    print("YES")
else:
    print("NO")