A = list(map(int, input().split()))
count = 0
for i in range(1,10):
    for j in A:
        if i == j:
            count += 1
    print(count, end=' ')
    count = 0