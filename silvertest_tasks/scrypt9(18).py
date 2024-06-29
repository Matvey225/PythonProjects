n = int(input())
def printTree(n):
    string = "o"
    space = " "
    count_string = 1
    flag = False
    for i in range(1, n + 1):
        print(space * (n - 2), string * count_string, sep="")
        n -= 1
        count_string += 2
printTree(n)