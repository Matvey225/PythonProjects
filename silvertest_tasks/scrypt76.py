a, b, c = map(int, input().split())
if a < b and b < c and a < c:
    print("on growth!")
else:
    print("dont on growth!")