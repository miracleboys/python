"""
作者：lrmy
日期：2021年10月30日
"""
c = 90
a = 30
print(c%a)#取模赋值运算符
print(c//a)#取整除赋值运算符

b = 3
a = 3
print(b**a)#幂赋值运算符

a={1,2,3,4,5,6,7}
if (n := len(a)) < 10:#海象运算符，可在表达式内部为变量赋值
    print(f"List is too long ({n} elements, expected <= 10)")
    print("List is too long ("+ str(n) +" elements, expected <= 10)")

x="a"
y="b"
print( x, end=" " )
print( y, end=" " )

a, b, c = 1, 2, "runoob"
print(a,b,c)

print(complex(3,1))

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'} #建立集合

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra') #每个元素分开，重复消去
b = set('alacazam')

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

del dict['one']  #删除字典的键
dict.clear() #清空字典
del dict #删除字典

Th = set(("a","b","c","d"))
Th.add('e')
print(Th)
Th.update({1,2},[3,4],'5')
print(Th)

Th.remove(1)
print(Th)
Th.discard('a')
print(Th)
Th.pop()
print(Th)

