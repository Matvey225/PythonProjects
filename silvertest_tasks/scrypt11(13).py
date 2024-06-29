n = int(input())
max = 0
min = 9
while n != 0:
    if n % 10 > max:
        max = n % 10
    if n % 10 < min:
        min = n % 10
    n = n // 10
print(max)
print(min)