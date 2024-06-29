n = int(input())
n1 = n
s = 0
while n != 0:
    s += n % 10
    n = n // 10
print("The sum of the digits of number", n1, "is", s)