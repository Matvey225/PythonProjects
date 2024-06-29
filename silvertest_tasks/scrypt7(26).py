n = int(input())
A = [0] * n
A = list(map(int, input(). split()))
count = 0
small = 100
flag = False
for i in range(0, len(A)):
    if A[i] < small and flag == False:
        small = A[i]
        count += 1
        flag = True
    elif A[i] < small and flag == True:
        small = A[i]
        count = 1
        flag = False
print(count)