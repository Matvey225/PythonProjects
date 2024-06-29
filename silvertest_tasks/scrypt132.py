x1, y1 = map(int, input(). split())
x2, y2 = map(int, input(). split())
x3, y3 = map(int, input(). split())
primary_diaganal_condition = ((x1 - y1) == (x2 - y2) and (x1 - y1) == (x3 - y3))
secondary_diaganal_condition = ((x1 + y1) == (x2 + y2) and (x1 + y2) == (x3 + y3))
primary_and_secondary_diagonal_condition = (x1 + y1) == (x2 + y2) or (x1 + y1) == (x3 + y3) and (x1 - y1) == (x2 - y2) and (x1 - y1) == (x3 - y3)
if primary_diaganal_condition or secondary_diaganal_condition or primary_and_secondary_diagonal_condition:
    print("double")
else:
    print("no")