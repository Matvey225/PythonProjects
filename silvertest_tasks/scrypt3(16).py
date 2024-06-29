n = int(input())
win = 0
rate = 1
for i in range (n):
    i = int(input())
    if i == 1:
        win += rate
        rate = 1
    elif i != 1:
        win -= rate
        rate *= 2
print(win)