s = input()
t = input()
c = ''
s1 = 0
for i in range(0, len(s)):
    s1 = s.find(t, i)
    if c != s1 and  s1 >= 0:
        c = s1
        print(c)