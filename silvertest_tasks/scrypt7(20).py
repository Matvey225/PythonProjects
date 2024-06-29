def stepen(val,p):
    if p<0:
        return stepen(1/val, -p)
    if p==0:
        return 1
    if p%2 == 0:
        return stepen(val*val, p/2)
    else:
        return val*stepen(val*val,(p-1)/2)
val = float(input())
p = float(input())
print(stepen(val,p))