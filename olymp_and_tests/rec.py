def rec(a):
    if (a>0): 
        rec(a-1)
    print(a)
a = int(input())
rec(a)