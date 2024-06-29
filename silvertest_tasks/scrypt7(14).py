n = int(input())
num = 0
count = 1
while n != 0:
    if num == n:
        count =+ 1
    elif num != n:
        count = 1
    num = n
    n = int(input())
print(count)