"""
作者：lrmy
日期：2021年10月09日
"""

message = input("Tell me somethiong, and I will repeat it back to you: ")
print(message)


#打印内容
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)  #用户输入
print("\nHello, "+ name + "!")


height = input("How tall are you, in inches？")
height = int(height)
if height >= 30:
    print('\nYou are tall enough to ride!')
else:
    print('\nYou will able to ride when you are will a little older.')


number = input("Enter a number, and I will tell you if it is even or odd:")
number = int(number)
if number%2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe nuumber "+str(number)+" is odd.")


promot = "\nTell me somethong, and I will repeat it back to you:"
promot = "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
promot += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I would love to go to "+city.title()+"!")

current_number = 0
while current_number <10:
    current_number +=1
    if current_number %2==0:
        continue
    print(current_number)

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.aqqend(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:#如果'cat'在列表中循环继续，直到没有
    pet.reomve('cat')
print(pets)

rseponses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    reponses[name] = response
    repeat = input("Would you like to let another perosn respond?(Yes/No)")
    if repeat == "No":
        polling_active = False
print("\n---Poll Results ---")
for name, response in rseponses.items():
    print(name + " would like to climb "+response+".")
