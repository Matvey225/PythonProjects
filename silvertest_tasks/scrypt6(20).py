def f(x):
    if x > 1:
        return x * f(x - 1)
    else:
        return 1
def c(n, k):
    first = f(n)
    second = f(k) * f(n - k)
    ans = first / second
    return int(ans)
n = int(input())
k = int(input())
print(c(n, k))