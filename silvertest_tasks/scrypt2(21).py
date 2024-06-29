import math
def nod(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == 0 and b == 0:
        return 0 
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a
def solve(a):
    a = int(input())
    for i in range(a):
        a += int(input())
    return math.gcd(a)
