x = float(input())
y = float(input())
day = 1
while y > x:
    x = x + x / 100 * 10
    day += 1
print(day)