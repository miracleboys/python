"""
作者：lrmy
日期：2021年10月21日
"""
class Dog(): #创建类
    def __init__(self, name, age): #相当于C++的构造函数
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_dog = Dog('while',6) #创建实例
print("My dog's name is "+my_dog.name.title()+".") #访问属性
print("My dog is "+str(my_dog.age)+" yaers old.")
my_dog.sit() #调用方法
my_dog.roll_over()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment(self,miles):
        self.odometer_reading += miles

my_new_car = Car('bwm','a4',2021)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment(100)
my_new_car.read_odometer()

class Battery():  #将实例用作属性
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(ElectricCar, self).__init__(make,model,year) #继承
        self.battery = Battery()   #将一个类作为属性
    def fill_gas_tank(self):       #与父类函数名相同，覆盖父类函数
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() #通过属性调用类的方法

from car import Car,ElectricCar   #从一个模板中导入多个类，在一个模板中导入另一个模板
my_new_car = Car('bwm','a4',2021) #直接使用模板的类
print(my_new_car.get_descriptive_name())
my_tesla = ElectricCar('tesla','model s',2021)
print(my_tesla.get_descriptive_name())

import car   #导入整个模板
my_new_car = car.Car('bwm','a4',2021)  #通过模板使用模板的类
print(my_new_car.get_descriptive_name())
my_tesla = car.ElectricCar('tesla','model s',2021)
print(my_tesla.get_descriptive_name())

