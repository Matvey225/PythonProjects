a = int(input())
if (a % 10) * (a // 10 % 10) * (a // 100) >= 100:
    print("YES")
else:
    print("NO")