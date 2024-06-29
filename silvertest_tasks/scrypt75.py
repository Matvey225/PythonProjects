n = int(input())
one = 0
ten = 0
sixty = 0
if n < 10:
    one = n
    ten = 0
    sixty = 0
    print(one, ten, sixty)
elif n >= 10 and n < 60 and n % 10 == 0:
    one = 0
    ten = n // 10
    sixty = 0
    print(one, ten, sixty)
elif n >= 10 and n < 60 and n % 10 != 0:
    one = 0
    ten = n // 10 + 1
    sixty = 0
    print(one, ten, sixty)
elif n >= 60 and n % 60 == 0:
    one = 0
    ten = 0
    sixty = n // 60
    print(one, ten, sixty)
elif n >= 60 and n % 60 != 0:
    one = 0
    ten = 0
    sixty = n // 60 + 1
    print(one, ten, sixty)