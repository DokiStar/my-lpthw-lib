name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
# 身高：英寸转厘米
print(f"He's {height * 2.54} centimeters tall.")
# 体重：磅转千克
print(f"He's {weight} pounds heavy.")
print(f"He's {weight * 0.45359237} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 个人练习

# round()函数，实现四舍五入
print(round(1.7333)) # 结果为2