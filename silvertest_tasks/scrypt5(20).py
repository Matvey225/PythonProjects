def CountDigit(n):          
    if n < 10:
        return 1
    else:
        return 1 + CountDigit(n//10)
n = int(input())
print(CountDigit(n)) 