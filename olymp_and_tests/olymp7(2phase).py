n = int(input())
i = 2
res = 0
while n != 1:
    if n % i == 0:
        n //= i
        res *= 10 
        res += i 
    else:
        i += 1
if res == i:
    print(-1)
else:
    print(res)