k = int(input())
flag = True
count = 0
rate = 1
last_rate = 0
for i in range(1, k + 1):
    if 1 <= i <= 9:
        count += 1
    else:
        global_length = len(str(i))
        length = len(str(i))
        while length != global_length // 2 and flag == True:
            last = (i % (10 ** rate)) // (10 ** last_rate)
            first = (i // (10 ** (length - 1))) % 10
            if last != first:
                flag = False
            length -= 1
            rate += 1
            last_rate += 1
        if flag == True:
            count += 1
        flag = True
        rate = 1
        last_rate = 0
print(count)