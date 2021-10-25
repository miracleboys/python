"""
作者：lrmy
日期：2021年10月25日
"""
import turtle as t
import random as r
t.speed(0)
t.colormode(255)

for i in range(20):

    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)

    x = r.randint(-220,220)
    y = r.randint(-50,220)

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.color(red,green,blue)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.right(90)
    t.forward(30)
    t.left(90)#画笔方向返回

t.done()