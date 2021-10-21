"""
作者：lrmy
日期：2021年10月20日
"""
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)

def show():
    print("Hello World!")