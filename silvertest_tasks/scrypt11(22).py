bit_str = input()
count_1 = 0
for s in bit_str:
    if s == '1':
        count_1 += 1
if count_1 % 2 == 0:
    bit_str += '0'
elif count_1 % 2 != 0:
    bit_str += '1'
print(bit_str)