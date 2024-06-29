xw1, yw1 = map(int, input(). split())
xw2, yw2 = map(int, input(). split())
xe1, ye1 = map(int, input(). split())
xe2, ye2 = map(int, input(). split())
w = 0
e = 0
if xw1**2 + yw1**2 < 5**2 and xw1**2 + yw1**2 != 0:
    w = w + 30
elif xw2**2 + yw2**2 < 5**2 and xw2**2 + yw2**2 != 0:
    w = w + 30
elif xw1**2 + yw1**2 >= 5**2 and xw1 > 0 and yw1 > 0 or xw1 < 0 and yw1 < 0:
    w = w + 20
elif xw2**2 + yw2**2 >= 5**2 and xw2 > 0 and yw2 > 0 or xw2 < 0 and yw2 < 0:
    w = w + 20
elif xw1**2 + yw1**2 >= 5**2 and xw1 > 0 and yw1 < 0 or xw1 < 0 and yw1 > 0:
    w = w + 15
elif xw2**2 + yw2**2 >= 5**2 and xw2 > 0 and yw2 < 0 or xw2 < 0 and yw2 > 0:
    w = w + 15
elif xw1 == 0 and yw1 == 0 or xw2 == 0 and yw2 == 0:
    w = w + 50
elif xe1**2 + ye1**2 < 5**2 and xe1**2 + ye1**2 != 0:
    e = e + 30
elif xe2**2 + ye2**2 < 5**2 and xe2**2 + ye2**2 != 0:
    e = e + 30
elif xe1**2 + ye1**2 >= 5**2 and xe1 > 0 and ye1 > 0 or xe1 < 0 and ye1 < 0:
    e = e + 20
elif xe2**2 + ye2**2 >= 5**2 and xe2 > 0 and ye2 > 0 or xe2 < 0 and ye2 < 0:
    e = e + 20
elif xe1**2 + ye1**2 >= 5**2 and xe1 > 0 and ye1 < 0 or xe1 < 0 and ye1 > 0:
    e = e + 15
elif xe2**2 + ye2**2 >= 5**2 and xe2 > 0 and ye2 < 0 or xe2 < 0 and ye2 > 0:
    e = e + 15
elif xe1 == 0 and ye1 == 0 or xe2 == 0 and ye2 == 0:
    e = e + 50
elif w > e:
    print("W", w)
elif e > w:
    print("E", e)
elif w == e:
    print("W=E", w)