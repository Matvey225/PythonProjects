n, z = map(int, input(). split())
answer = 0
while n != 0:
    if (n % 10) % z == 0:
        answer += 1
    n //= 10
print(answer)