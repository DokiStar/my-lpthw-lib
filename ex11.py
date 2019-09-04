print("How old are you?", end=' ')
# input默认返回字符串类型
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 更多输入
str = input("Input some text here: ")
str2 = input("more things here: ")
print("The text you input is", str + str2)

# 类似代码
name = input("Your name: ")
univiersity = input("Your university: ")

print("Hello,", name, "\nyour university is", univiersity)

# input转换为数字，使用int()强制转换
num1 = int(input("Input a number here: "))
num2 = int(input("Input another number here: "))

print("num1 + num2 =", num1 + num2)
