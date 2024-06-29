A = list(map(int, input().split()))
h = int(input())
count = 1
if h <= A[len(A)-1]:
    print(len(A)+1)
else:
    for i in range(0, len(A)):
        if h > A[i]:
            print(count)
            break
        else:
            count += 1