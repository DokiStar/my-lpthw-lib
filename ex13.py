from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 更多参数
from sys import argv
zero, ichi, ni, san, yon = argv
print("zero go wa:", zero)
print("ichi go wa:", ichi)
print("ni go wa:", ni)
print("san go wa:", san)
print("yon go wa:", yon)

# 更少参数
from sys import argv
x, y = argv
print("x =", x)
print("y =", y)

# input和argv一起用
from sys import argv
script, first, second = argv
second = input("Input the second argument: ")
third = input("Input the third argument: ")
print(f"script: {script}, 1st: {first}, 2nd: {second}, 3rd: {third}")
