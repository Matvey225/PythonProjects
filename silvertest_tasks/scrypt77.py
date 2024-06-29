n = int(input())
if n % 10 == n // 10 % 10 and n % 10 == n // 100 and n // 10 % 10 == n // 100:
    print("YES")
elif n % 10 != n // 10 % 10 or n % 10 != n // 100 or n // 10 % 10 != n // 100:
    print("NO")