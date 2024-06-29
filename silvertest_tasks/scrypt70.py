x, y = map(float, input(). split())
if x**2 + y**2 > 4:
    if x > 2:
        if y < 0:
            if y < x:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")