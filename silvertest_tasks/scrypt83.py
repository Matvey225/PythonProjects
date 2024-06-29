x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if x1 + 1 == x2 or x1 - 1 == x2:
    print("YES")
if y1 + 1 == y2 or y1 - 1 == y2:
    print("YES")
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")