n = int(input())
sum = 0
max = 0
rate = 0
for i in range (1, n+1):
    for j in range(1, n+1):
        if i % j == 0:
            sum += j
    if sum > max:
        max = sum
        rate = i
    sum = 0
print(rate)