"""
作者：lrmy
日期：2021年10月22日
"""
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