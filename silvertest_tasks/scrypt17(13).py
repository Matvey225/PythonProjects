n = int(input())
answer = 0
while n != 0:
    if n > 10 and n < 100 and n % 10 == 3:
        answer = answer + 1
    n = int(input())
print(answer)