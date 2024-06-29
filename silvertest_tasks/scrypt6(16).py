first, second, n = map(int, input().split())
grow = second - first
for i in range(n):
    print (first, end=" ")
    first += grow