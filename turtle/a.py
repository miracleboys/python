"""
作者：lrmy
日期：2021年10月25日
"""
#第三方库
import turtle as t

#画笔速度
t.speed(0)

#画笔颜色
t.color('green')

for i in range(36):
    t.right(10)  # 画笔方向
    t.circle(100) #画圆圈 大小

t.done()#保持屏幕显示