n = int(input())
i = 0
k = 0
j = 437
flag = False
while i < n:
    i += 1
    high= int(input())
    if high <= j and flag == False:
        k = i
        flag = True
if k == 0:
    print("No crash")
else:
    print("Crash", k)