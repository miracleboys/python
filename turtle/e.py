"""
作者：lrmy
日期：2021年10月25日
"""
import turtle as t
import random as r

t.colormode(255)
t.speed(0)
t.bgcolor('black')

t.pensize(100)

t.goto(-400,200)
t.forward(800)

t.color(50,50,50)
t.penup()
t.goto(-400,100)
t.pendown()
t.forward(800)

t.color(75,75,75)
t.penup()
t.goto(-400,0)
t.pendown()
t.forward(800)

t.color(100,100,100)
t.penup()
t.goto(-400,-100)
t.pendown()
t.forward(800)

t.color(125,125,125)
t.penup()
t.goto(-400,-200)
t.pendown()
t.forward(800)

t.color(150,150,150)
t.penup()
t.goto(-400,-300)
t.pendown()
t.forward(800)

t.pensize(3)
t.color('yellow')

for i in range(7):
    x =r.randint(-300,300)
    y =r.randint(0,250)

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.left(30)
        t.forward(15)
        t.right(120)
    t.end_fill()
    t.left(35)

t.done()