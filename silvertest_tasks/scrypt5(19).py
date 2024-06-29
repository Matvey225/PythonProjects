import math
def SumOfDivisions(n):
    sum = 0
    for i in range(1, int(n**(0.5)) +1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum - n
def isPerfectNumber(n):
    return(n == SumOfDivisions(n))
N = int(input())
if isPerfectNumber(N):
    print("YES")
else:
    print("NO")