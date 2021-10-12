"""
作者：乱入梦魇
日期：2021年10月07日
"""

users = ['acc','Ghs','hJk','BBC']
for user in users:
    if user == 'acc':
        print(user.upper())
    else:
        print(user.lower())

car = 'bwm'
print(car == 'bwm')
print(car == 'audi')
print(car == 'BWM')
print(car.upper() == 'BWM')
print(car != 'abc')

age = 20
print(age == 20)
print(age > 22)
print(age < 22)

age = 20
if age < 22 and age >18:
    print('hello')

age = 27
if age > 22 or age < 18:
    print('bye')

users = ['acc','Ghs','hJk','BBC']
user = 'BBC'
if user in users:
    print('Yes')

if user not in users:
    print('No')
else:
    print('Yes')

print(users[0:3])
if user  in user[0:3]:
    print('Yes')
else:
    print('No')
for user in users[0:3]:
    print(user)

age = 20
if age < 5:
    print(1)
elif age <= 20:
    print(2)
elif age < 60:
    print(3)
else:
    print(5)

age = 20
if age > 5:
    print(1)
elif age >= 20:
    print(2)
elif age > 60:
    print(3)
else:
    print(5)

users = []
if users:
    for user in users:
        print(user)
else:
    print('kong')

mycars = ['bwm','byd','ad']
yourcars = ['bwm','acc','ad']
for car in mycars:
    if car in yourcars:
        print(car+' Me too')
    else:
        print(car+' No')

my = {'name':'Bob','age':12}
print(my['name'])
print(my["age"])

a = my['name']
print(a)

my['address'] = 'nc'
print(my)

you = {}
you['name'] = 'Ali'
you['age']  = 20
print(you)

you['age'] = 15
print(you)

del you['age']
print(you)

ages = {
    'Abs' : 10,
    'Bob' : 12,
    'Ucc' : 20

}

user = {
    'name':'ncc',
    'job':'work',
    'address':'nc'
}

for key,value in user.items():
    print(key +' : '+value)


for use in user:
    print(use)

for use in user.keys():
    print(use)

for use in sorted(user.keys()):
    print(use)

for use in user:
    print(user[use])

for use in user.values():
    print(use)

for use in set(user.values()):
    print(use)

user_0 = {'name':'A','age':12}
user_1 = {'name':'B','age':22}
user_2 = {'name':'C','age':41}
users = [user_0,user_1,user_2]
for user in users:
    print(user)

aliens = []
for alien_num  in range(30):
    new_alien = {'color' : 'green','point':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of alien: '+str(len(aliens)))

pizza = {
    'crust':'thick',
    'topping':['cheese','mushroom']
}
print(pizza)
print(pizza['topping'])

favorite_languages = {
    'jen':['c','go'],
    'sara':['java'],
    'bob':['python','javascript'],
    'phil':['php','c']
}
for name ,languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + ' lieks '+ languages[0] )
    else:
        print(name.title() + ' lieks ')
        for language in languages:
            print(language)

users = {
    'aeinstein':{
        'first' :'albert',
        'last' : 'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}
print(users)
print(users['mcurie'])
for username , user_info in users.items():
    print('\nUsername: '+username)
    full_name = user_info['first']+' '+user_info['last']
    location = user_info['location']
    print('\tFull name: '+full_name.title())
    print('\tLocation: '+location.title())
print(len(users))