s = input()
i, j = map(int,input().split())
second_s = ''
new_s = ''
third_s = ''
for f in range(0, i-1):
    second_s += s[f]

for x in range(j -1, i -2, -1):
    new_s += s[x]

for z in range(j, len(s)):
    third_s += s[z]
print(second_s + new_s + third_s)