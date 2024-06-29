import turtle as t
from time import sleep


def square(obj):
    for i in range(4):
        obj.forward(100) 
        obj.left(90)
    sleep(1)
def triangle(obj):
    for i in range(3):
        obj.forward(100)
        obj.left(120)


obj = t.Turtle()
obj.speed(30)

# color_palate = ['red', 'blue', 'green', 'yellow']
# for i in range(4):
#     obj.color(color_palate[i])
#     square(obj)
#     obj.left(90)
# sleep(5)

# color_palate = ['red', 'orange', 'yellow', 'green', 'blue']
# for i in range(60):
#     obj.color(color_palate[i % 5])
#     obj.begin_fill()
#     obj.circle(30)
#     obj.end_fill()
#     obj.fillcolor('red')
#     obj.right(10)

color_palette = ['red', 'orange', 'yellow', 'green', 'blue']
for i in range(60):
    obj.color(color_palette[i % 5])
    obj.begin_fill()
    triangle(obj)
    obj.end_fill()
    obj.right(10)

sleep(5)
