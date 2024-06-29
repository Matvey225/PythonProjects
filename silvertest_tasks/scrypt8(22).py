s = input()
snew = ''
for c in s:
    if c == '.':
        c = '0'
        snew += c
    elif c == 'X':
        c = "1"
        snew += c
print(snew)