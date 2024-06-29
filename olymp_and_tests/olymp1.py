n = int(input())
count_l = 0
count_k = n
time = 0

if n == 2:
    print("-1")
while count_l != count_k:
    l = count_k - count_l
    if l > 7:
        count_l += 5
        time += 1
    elif l == 7:
        count_l += 4
        time += 1
    elif l == 6:
        count_l += 3
        time += 1
    elif l == 5:
        count_l += 5
        time += 1
    elif l == 4:
        count_l += 4
        time += 1
    elif l == 3: 
        count_l += 3
        time += 1
    elif l == 2:
        print("-1")
    elif l == 1:
        print("-1")    
print(time)