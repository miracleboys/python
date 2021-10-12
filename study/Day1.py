"""
作者：乱入梦魇
日期：2021年10月06日
"""
str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = """人生苦短，
我用python"""
str4 = '''人生苦短，
我用python'''

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))

name = '张三'
age = 20
print('我是'+name+',今年'+str(age)+'岁')

# a = input('你叫什么名字？')
# print(a)

num1 = input('请输入一个数')
num2 = input('请输入一个数')
print(int(num1)+int(num2))