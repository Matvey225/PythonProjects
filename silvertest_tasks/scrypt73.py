import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == x2) or (y1 == y2):
    print("YES")
elif abs(x1 - y1) == abs(x2 - y2):
    print("YES")
elif abs(x1 + y1) == abs(x2 + y2):
    print("YES")
elif x1 == x2 and y1 == y2:
    print("NO")
elif ((x1 == x2) or (y1 == y2)):
    print("NO")