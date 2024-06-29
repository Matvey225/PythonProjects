def m2(a, b):
    if a < b:
        m2 = a
    else:
        m2 = b
    return m2
def m3(a, b, c):
    if a < b and a < c:
        m3 = a
    elif b < a and b < c:
        m3 = b
    elif c < a and c < b:
        m3 = c
    return m3
a, b, c = map(int, input().split())
print (m3(a, b, c))