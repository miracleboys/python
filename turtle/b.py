"""
作者：lrmy
日期：2021年10月25日
"""
import turtle as t

t.speed(0)
#画笔粗细
t.pensize(7)

t.color('black')
t.circle(75)

t.penup()#画笔抬笔
t.goto(-160,0)#画笔位置
t.pendown()#画笔下笔

t.color('blue')
t.circle(75)

t.penup()
t.goto(160,0)
t.pendown()

t.color('red')
t.circle(75)

t.penup()
t.goto(80,-100)
t.pendown()

t.color('green')
t.circle(75)

t.penup()
t.goto(-80,-100)
t.pendown()

t.color('yellow')
t.circle(75)

t.color('black')
t.penup()
t.goto(-100,180)
t.pendown()
t.write('北京 2018',font=('YouYuan',32))

t.done()#保持屏幕显示