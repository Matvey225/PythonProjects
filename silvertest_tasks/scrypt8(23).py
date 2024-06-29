s = input()
s1 = ''
count = 0
flag = True
lenght_str = len(s)
count_elem = 0
count_of_right_slash = 0
while count_elem != lenght_str:
    if s[count_elem] != '/':
        s1 += s[count_elem]
        count_of_right_slash = 0
    elif s[count_elem] == '/':
        count_of_right_slash += 1
        if count_of_right_slash == 1:
            print(s1)
        s1 = ''
    count_elem += 1
print(s1)