s = input()
k = int(input())
new_s = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s:
    new_code = alphabet.find(i) - k
    new_s += alphabet[new_code]
print(new_s)