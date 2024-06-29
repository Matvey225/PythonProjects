n, z = map(int, input(). split())
answer = 0
while n != 0:
    if (n % 10) > z:
        answer += n % 10
    n //= 10
print(answer)