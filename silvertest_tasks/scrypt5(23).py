s = input()
new_s = ''
index_1 = s.find('h')
index_2 = s.rfind('h')
print(s[:index_1] + s[index_2 +1:])