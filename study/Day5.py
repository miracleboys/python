"""
作者：lrmy
日期：2021年10月15日
"""

# #函数传递信息
# def greet_user(username):#形参
#     print("Hello, "+username.title()+"!")
# greet_user('bob')#传递实参
#
# def describe_pet(animal_type,pet_name):
#     print("\nI have a "+animal_type+".")
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
# describe_pet('cat','mimi')#实参顺序
# describe_pet('dog','wawa')
# describe_pet('dog',pet_name='wawa')     #关键字参数位于位置参数后面
# #describe_pet(animal_type='dog','wawa')   错误
# describe_pet(animal_type='hamster',pet_name='harry')#关键字实参，实参顺序无关
# describe_pet(pet_name='harry',animal_type='hamster')
#
# def describe_pet(pet_name,animal_type='cat'):#默认参数跟随在非默认参数后面
#     print("\nI have a "+animal_type+".")
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
# describe_pet(pet_name='willie')
# describe_pet('willie')
# describe_pet('harry','hamster')
# describe_pet('harry',animal_type='hamster')  #关键字参数位于位置参数后面
# #describe_pet(pet_name='harry','hamster')     错误
# describe_pet(pet_name='harry',animal_type='hamster')#关键字实参，实参顺序无关
# describe_pet(animal_type='hamster',pet_name='harry')
#
# def get_formatted_name(first_name,middle_name,last_name):
#     full_name = first_name + ' '+middle_name+' '+last_name
#     return full_name.title(); #返回值
# musician = get_formatted_name('john','lee','hook')
# print('\n'+musician)
#
# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name = first_name + ' '+middle_name+' '+last_name
#     else:
#         full_name =first_name + ' '+last_name
#     return full_name.title()
# musician = get_formatted_name('jimi','hank')
# print('\n'+musician)
# musician = get_formatted_name('john','lee','hook')
# print('\n'+musician)
#
# def build_person(first_name, last_name,age=''):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person;  #返回字典
# musician = build_person('jion','hend',age=22)
# print(musician)
#
# def get_formatted_name(first_name,last_name):
#     full_name = first_name+' '+last_name
#     return full_name
# while True: #while循环
#     print("\nPlaese tell me your name: ")
#     print("(enter 'Q' at any time to quit)")
#     f_name = input("First_name: ")
#     if f_name == 'Q':
#         break
#     L_name = input("Last name: ")
#     if L_name == 'Q':
#         break
#     formatted_name = get_formatted_name(f_name,L_name)
#     print("\nHeelo, "+formatted_name+"!")
#
# def greet_users(names):
#     for name in names:
#         msg = "Hello, "+name.title()+"!"
#         print(msg)
# usernames = ['hank','coco','may']#传递列表
# greet_users(usernames)
#
#
#
# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)
#
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following topping:")
#     for topping in toppings:
#         print("-"+topping)
# make_pizza('pepperoni')
# make_pizza('pepperoni','mushrooms','cheese')

def make_pizza(size,*toppings):#位置实参，关键字实参，任意数量实参
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza(12,'pepperoni')
make_pizza(15,'pepperoni','mushrooms','cheese')

def build_profile(first,last,**user_info):#任意数量的关键字实参
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():#返回键-值对列表
        profile[key] = value
    return profile
user_profile = build_profile('abb','ell',location = 'princeton',field = 'physics')
print('\n'+user_profile)

import pizza
make_pizza(12,'pepperoni')
make_pizza(15,'pepperoni','mushrooms','cheese')




