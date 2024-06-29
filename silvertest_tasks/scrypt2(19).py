def numberOfDivisors(n):
    num = 0
    for i in range(1, n+1):
        if n % i == 0:
            num += 1
    return num
n = int(input())
print(numberOfDivisors(n))