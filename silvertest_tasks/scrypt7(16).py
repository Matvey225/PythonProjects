n = int(input())
sum = 0
num1 = 1
num2 = 2
flag = True
for i in range(n-1):
    if flag == True:
        print(num1, "*", num2, sep="", end="")
    elif flag == False:
        print("+", num1, "*", num2, sep="", end="")
    sum += (num1 * num2)
    num1 += 1
    num2 += 1
    flag = False
print("=", sum, sep="")