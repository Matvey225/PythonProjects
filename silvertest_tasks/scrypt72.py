a = int(input())
b = int(input())
if a % 10 == a // 10 % 10:
    if b == 1:
        print("YES")
if a % 10 != a // 10 % 10:
    if b != 1:
        print("YES")
if a % 10 == a // 10 % 10:
    if b != 1:
        print("NO")
if a % 10 != a // 10 % 10:
    if b == 1:
        print("NO")