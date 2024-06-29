n = int(input())
A = [0]* n
for i in range(n):
    A[i] = int(input())
s = input().split() 
B = [int(i) for i in s] 
print(*A)
print(*B)