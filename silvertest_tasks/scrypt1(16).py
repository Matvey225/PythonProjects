a = "+___"
b = "|j /"
c = "|__\\"
d = "|   "
n = int(input())
for i in range(4):
    for j in range(n):
        if i == 0:
            print(a, "", end="")
        if i == 1:
            print("|", j+1," / ", "", end="", sep="")
        if i == 2:
            print(c, "", end="")
        if i == 3:
            print(d, "", end="")
    print("")