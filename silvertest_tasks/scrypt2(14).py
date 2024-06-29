x = int(input())
p = int(input())
y = int(input())
year = 0
while y > x:
    x *= 1 + (p / 100)
    x = int(100 * x) / 100
    year += 1
print(year)