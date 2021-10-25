"""
作者：lrmy
日期：2021年10月25日
"""
import turtle as t

t.speed(0)

t.penup()
t.goto(0,-200)
t.pendown()
t.color('red')
t.begin_fill()#开始填充
t.circle(200)
t.end_fill()#结束填充

t.penup()
t.goto(0,-150)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(150)
t.end_fill()

t.penup()
t.goto(0,-100)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0,-50)
t.pendown()
t.color('blue')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-40,10)
t.pendown()
t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

t.done()