n = int(input())
if n <= 6:
    print(1)
else:
    print((((n - 6)+ 4 - 1) // 4) + 1)