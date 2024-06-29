n = int(input())
i = 0
ans = 0
longest = 0
while i < n:
    temp = int(input())
    if temp > 0:
        ans += 1
        longest = max(longest, ans)
    else:
        ans = 0
    i += 1
print(longest)