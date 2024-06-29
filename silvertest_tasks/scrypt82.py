a = int(input())
b = a % 10
if (a > 9) and (a < 20) or (a > 110) or (b > 4) or (b == 0):
    print("Vam", a, "let")
elif a == 1 or b == 1:
    print("Vam", a, "god")
else:
    print("Vam", a, "goda")