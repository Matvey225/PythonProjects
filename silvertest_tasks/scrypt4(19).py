def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
    return a + b
a, b = map(int, input(). split())
print(NOD(a,b))  