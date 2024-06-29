n, m = map(int, input().split())
A = [ [0]*m for i in range(n) ]
prev = 1
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            A[i][j] = 0
        else:
            A[i][j] = 1
        
for row in A:            
    for elem in row:     
        print(elem, end = ' ')
    print()