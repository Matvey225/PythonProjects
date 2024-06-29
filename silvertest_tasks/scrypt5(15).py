n = int(input())
first = n
answer = 0
while n != 0:
    if n > first:
        answer += 1
    n = int(input())
print(answer)