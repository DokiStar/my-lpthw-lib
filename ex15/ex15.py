# 从系统导入命令行参数argv
from sys import argv

# 定义两个变量，script（脚本）和filename（文件名），两个变量都由命令行参数进行赋值
script, filename = argv

# 定义一个变量txt（文本），由open()函数获取文件对象并赋值给txt
txt = open(filename)
# 利用变量filename，输出文件名
print(f"Here's your file {filename}:")
# 利用变量txt，使用read()函数读取文件对象，输出文件内容
print(txt.read())

# 输出一行字符串，要求重新输入文件名（完整文件名）
print("Type the file name again:")
# 定义一个变量file_again（文件名再来一次），从键盘输入
file_again = input("> ")

# 定义一个变量txt_again（文本再来一次），open()函数读取file_again所对应文件对象，赋值给txt_again
txt_again = open(file_again)

# 输出txt_again对应的内容
print(txt_again.read())

# 对象用完，将其关闭
txt.close()
txt_again.close()

# 在终端下打开python，在提示符下输入以下指令以打开文件
print(open("ex15_sample.txt").read())