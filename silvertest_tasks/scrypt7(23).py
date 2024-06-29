s = input()
count = 0
new_s = ''
for i in s:
    if i == ' ':
        count += 1
    elif i != ' ':
        count = 0
    if count > 1:
        i = ''
    new_s += i
print(new_s)