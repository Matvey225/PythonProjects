n = int(input())
count = 0
while n != 0:
    if n % 3 == 0:
        count = count + 1
    n = int(input())
print(count)