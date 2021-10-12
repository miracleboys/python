"""
作者：乱入梦魇
日期：2021年10月06日
"""
name = "EvE Love"
print(name.upper())
print(name.lower())
print(name.title())

language = '  python  '
print(language+'abc')
print(language.rstrip()+'abc')
print(language.lstrip()+'abc')
print(language.strip()+'abc')

age = 20
message = "Happy "+str(age)+"rd Birthday"
print(message)

users = ['Aoc','Bod','ssn','GOD']
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users[2].title())
print(users[-1].title())

users = ['Aoc','Bod','ssn','GOD'] #修改列表元素
print(users[0].title())
users[0] = 'Abc'
print(users[0].title())

users = ['Aoc','Bod','ssn','GOD']
print(users)
users.append("Cat")
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users)
users.insert(0,'acc')
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users)
del users[1]
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users)
user = users.pop()
print(user)
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users)
user = users.pop(0)
print(user)
print(users)

users = ['Aoc','Bod','ssn','GOD']
print(users)
a = 'ssn'
users.remove(a)
print(users)

users = ['Aoc','Bod','ssn','GOD','ssn']
print(users)
a = 'ssn'
users.remove(a)
print(users)

users = ['coc','Bod','ssn','avv','AXX','GOD']
print(users)
users.sort()
print(users)

users = ['coc','Bod','ssn','avv','AXX','GOD']
print(users)
users.sort(reverse = True)
print(users)

users = ['coc','Bod','ssn','avv','AXX','GOD']
print(users)
print(sorted(users))
print(users)

users = ['coc','Bod','ssn','avv','AXX','GOD']
print(users)
print(sorted(users,reverse = True))
print(users)

nums = [123,12,54]
print(nums[1])
nums.sort()
print(nums)

cars = ['bmw','audi','toya','byd']
print(cars)
cars.reverse()
print(cars)

cars = ['bmw','audi','toya','byd']
print(len(cars))

cars = ['bmw','audi','toya','byd']
for car in cars:
    print('I Like '+car)
    print('Me too')
print('I donot like it')

for num in range(1,6):
    print(num)
nums = list(range(1,6))
print(nums)
nums = list(range(2,7,2))
print(nums)

nums = []
for num in range(1,6):
    nums.append(num**2)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

nums = [num**2 for num in range(1,6)]
print(nums)

for num in range(1,1):
    print(num)

users = ['coc','Bod','ssn','avv','AXX','GOD']
print(users[0:3])
print(users[1:4])
print(users[1:])
print(users[:3])
print(users[-3:])

for user in users[0:3]:
    print(user.title())

users = ['coc','Bod','ssn','avv','AXX','GOD']
users2 = users[:]
users.append('bbb')
users2.append('aaa')
print(users)
print(users2)

users = ['coc','Bod','ssn','avv','AXX','GOD']
users2 = users
users.append('bbb')
users2.append('aaa')
print(users)
print(users2)

users = ('a','b','c')
print(users)
print(users[0])
# users[0] = 'v'