# 巩固练习2：使用read和argv读取刚才新建的文件
from sys import argv

script, filename = argv

target = open(filename)

print(target.read())

target.close()