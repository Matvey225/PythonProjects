def sumofdev(n):
    sum = 0
    for i in range(1, int(n**(0.5)) +1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum - n
def isfriendly(a, b):
    if sumofdev(a) == b and sumofdev(b) == a:
        return "YES"
    else:
        return "NO"
a, b = map(int, input().split())
print(isfriendly(a, b))