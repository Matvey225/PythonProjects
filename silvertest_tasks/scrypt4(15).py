x = int(input())
n = int(input())
answer = 0
while n != 0:
    if n > x:
        answer += n
    n = int(input())
print(answer)