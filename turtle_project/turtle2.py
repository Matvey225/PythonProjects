import turtle as t
from time import sleep


def wall_1(obj):
    obj.color(color_palete[0])
    obj.begin_fill()
    for i in range(2):
        obj.forward(360) 
        obj.left(90)
        obj.forward(180)
        obj.left(90)
    obj.end_fill()

def window(obj):
    obj.color(color_palete[2])
    obj.begin_fill()
    for i in range(2):
        obj.forward(50) 
        obj.left(90)
        obj.forward(120)
        obj.left(90)
    obj.end_fill()


def door(obj):
    obj.color(color_palete[1])
    obj.begin_fill()
    for i in range(2):
        obj.forward(65) 
        obj.left(90)
        obj.forward(130)
        obj.left(90)
    obj.end_fill()

def triangle(obj):
    obj.color(color_palete[3])
    obj.begin_fill()
    for i in range(3):
        obj.forward(120)
        obj.left(120)
    obj.end_fill()

def rectangle(obj):
    obj.color(color_palete[4])
    obj.begin_fill()
    for i in range(2):
        obj.forward(40) 
        obj.left(90)
        obj.forward(90)
        obj.left(90)
    obj.end_fill()



obj = t.Turtle()
obj.speed(10)
color_palete = ['yellow', 'brown', 'blue', 'green', 'gray', 'black']

obj.penup()
obj.backward(170)
obj.right(90)
obj.forward(100)
obj.left(90)
obj.pendown()

wall_1(obj)

obj.penup()
obj.forward(20)
obj.left(90)
obj.forward(40)
obj.right(90)
obj.pendown()
window(obj)

obj.penup()
obj.right(90)
obj.forward(40)
obj.left(90)
obj.forward(100)
obj.pendown()

obj.left(90)
obj.forward(180)
obj.left(30)
triangle(obj)
obj.left(60)

obj.penup()
obj.forward(60)
obj.right(90)
obj.forward(30)
obj.right(90)
obj.color(color_palete[2])
obj.begin_fill()
obj.circle(20)
obj.end_fill()
obj.color(color_palete[3])
obj.left(90)
obj.forward(75)
obj.right(90)
obj.pendown()

obj.forward(240)
obj.right(120)
triangle(obj)

obj.penup()
obj.left(120)
obj.backward(70)
obj.right(90)
obj.forward(20)
obj.left(90)
rectangle(obj)

obj.penup()
obj.right(90)
obj.forward(85)
obj.pendown()
obj.color(color_palete[2])
obj. forward(180)

obj.penup()
obj.right(90)
obj.forward(100)
obj.right(180)
obj.pendown()
door(obj)

obj.penup()
obj.forward(10)
obj.left(90)
obj.forward(60)
obj.pendown()
obj.color(color_palete[5])
obj.right(90)
obj.circle(5)

sleep(3)