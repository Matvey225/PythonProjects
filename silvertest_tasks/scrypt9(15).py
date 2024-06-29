n = int(input())
max = float('-inf')
min = float('inf')
while n > 0:
    num = n % 10
    if num % 2 == 0:
        if num < min:
            min = num
        if num > max:
            max = num
    n //= 10
if max == float('-inf') or min == float('inf'):
    print("NO")
else:
    print(min, max)