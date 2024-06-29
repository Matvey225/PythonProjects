n, m = map(int, input().split())
A = []
B = []
for i in range(m):
    B.append([0]*n)
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        B[i][j] = A[j][i]
for row in B:            
    for elem in row:     
        print(elem, end = ' ')
    print()