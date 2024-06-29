x, y = map(float, input(). split())
if x < 2 and x > -2 and y > -7 and y < 0:
    print("Y")
elif x < 5 and x > -5 and y < -7 and y > -9:
    print("G")
elif x**2 + y**2 < 5**2 and y > 0:
    print("R")
elif x**2 + y**2 == 5**2 and y > 0 or x >= -5 and x <= 5 or x == -2 and y <= 0 and y >= -7 or x == 2 and y <= 0 and y >= -7 or x == -5 and y <= -7 and y >= -9 or x == 5 and y <= -7 and y >= -9 or y == -7 and x <= 5 and x >= -5 or y == -9 and x <= 5 and x >= -5:
    print ("B")
elif (y < -9) or (x > 2 and y < 0 and y > -7) or (x < -2 and y > -7 and y < 0) or (x > 5 and y < -7 and y > -9) or (x < -5 and y < -7 and y > -9) or (x**2 + y**2 > 5**2 and y > 0):
    print("W") 