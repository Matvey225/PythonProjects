answer = 0
n = 1
flag = False
while n != 0:
    n = int(input())
    if flag == False:
        answer = n
        flag = True
    if n != 0:
        if n % 2 == 0:
            if n >= answer:
                answer = n
if answer % 2 != 0:
    answer = 0
print(answer)