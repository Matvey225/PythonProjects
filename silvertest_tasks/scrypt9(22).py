s = input()
snew = ''
for c in s:
    if c == 'a':
        c = 'b'
    elif c == 'b':
        c = 'a'
    elif c == 'A':
        c = 'B'
    elif c == 'B':
        c = 'A'
    snew += c
print(snew)