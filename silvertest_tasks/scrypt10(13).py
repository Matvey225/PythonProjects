N = int(input())
k = int(input())
am = 0
while N != 0:
    if N % 10 == k:
        am = am + 1
    N = N // 10
print(am)