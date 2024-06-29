def numberOfOnes(N):
    b = bin(N)
    count = 0
    for i in (b):
        if i == '1':
            count += 1
    return count
N = int(input())
k = numberOfOnes(N)
print(k)