a = int(input())
b = int(input())
c = int(input())
d = int(input())
mr = a + 1
mb = b + 1
nr = c + 1
nb = d + 1
if mr < mb:
    M = mr
    N = nr
elif mb < mr:
    M = mb
    N = nb
print(M, N)