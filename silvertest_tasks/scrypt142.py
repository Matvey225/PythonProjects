a = ":)\_____/(:"
b = " {(@)v(@)} "
c = " {|~- -~|} "
d = " {/^'^'^\} "
e = " ===m-m=== "
n = int(input())
for i in range(5):
    for j in range(n):
        if i == 0:
            print(a, "", end="")
        if i == 1:
            print(b, "", end="")
        if i == 2:
            print(c, "", end="")
        if i == 3:
            print(d, "", end="")
        if i == 4:
            print(e, "", end="")
    print("")