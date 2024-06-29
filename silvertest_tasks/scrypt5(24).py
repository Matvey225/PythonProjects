s = input()
count = 0
for i in range(0, len(s)):
    if s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '7':
        count += 0
    elif s[i] == '6' or s[i] == '9' or s[i] == '0':
        count += 1
    elif s[i] == '8':
        count += 2
print(count)