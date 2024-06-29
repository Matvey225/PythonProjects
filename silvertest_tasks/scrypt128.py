t, n, p = map(int, input().split())
end = n * (1 + p / 100)**t
print(end)