x1, y1 = map(int, input(). split())
x2, y2 = map(int, input(). split())
x3, y3 = map(int, input(). split())
if abs(x1 - y1) == abs(x2 - y2) and abs(x1 - x3) == abs(y1 - y3):
    print("double")
elif abs(x1 - y1) != abs(x2 - y2) and abs(x1 - x3) != abs(y1 - y3):
    print("no")