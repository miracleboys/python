"""
作者：lrmy
日期：2021年10月22日
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())#rstrip() lstrip() strip()
    print("Hello")

file_path = r'D:\成绩单.txt' #以原始字符串指定路径

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object: #逐行读取
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines() #读取每一行存储到列表
    pi_string = ''
for line in lines:
    pi_string += line.strip()#删除换行符
print(pi_string)
print(len(pi_string))

filename = 'programming.txt'
with open(filename,'w') as file_object:
    #'r'读取模式，默认模式
    # 'w'写入模式，会清空之前的数据
    # 'a'附加模式，不会清空文件数据，写入的数据添加到文件末尾，没有文件会新建
    # 'r+'读取与写入模式
    file_object.write("I love python!\n")
    file_object.write("You like Python!\n")#多行写入
    file_object.write(str(10086))#写入数值数据必须先用str()函数转化为字符串格式

#异常
try:#提高抵御错误的能力
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    with open('alice.txt') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass   #出错时一声不吭

#JSON格式
import json
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
# with open(filename,'w') as f_obj:
#     json.dump(numbers,f_obj)   #存储数字列表
with open(filename) as f_obj:
    numbers = json.load(f_obj)  #读取数字列表
print(numbers)

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNOtFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back, "+username+"!")
greet_user()