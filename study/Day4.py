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


