a = int(input())
e = a % 10
d = a // 10 % 10
s = a // 100 % 10
t = a // 1000 % 10
part1 = s*1000 + t*100
part2 = e*10 + d
all = part1 + part2
print(all)