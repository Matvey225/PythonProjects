import math
def sum():
    return number1 + number2
def dif():
    return number1 - number2
def mult():
    return number1 * number2
def dev():
    return number1 / number2
def pow():
    return number1 ** number2
def sqrt():
    return math.sqrt(number1)
def dev_rem():
    return number1 % number2
def dev_int():
    return number1 // number2
while input("введите yes, чтобы продолжить -> ") == 'yes':
    flag = False
    answer = "ответ ->"
    number1 = int(input("введите первое число -> "))
    operation = input("введите операцию (+, -, *, /, **, sqrt, %, //) -> ")
    if operation == "sqrt":
        flag = True
    if not flag:
        number2 = int(input("введите второе число -> "))
    if operation == "+":
        print(answer, sum())
    elif operation == "-":
        print(answer, dif())
    elif operation == "*":
        print(answer, mult)
    elif operation == "/":
        print(answer, dev())
    elif operation == "**":
        print(answer, pow())
    elif operation == "sqrt":
        print(answer, sqrt())
    elif operation == "%":
        print(answer, dev_rem())
    elif operation == "//":
        print(answer, dev_int())
    else:
        print("операция не предусмотрена")