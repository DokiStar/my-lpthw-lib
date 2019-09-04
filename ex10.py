tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# 使用3个单引号的块注释
print('''
I'll do a list:
\t"* Cat food"
\t""* Fishies""
\t"""* Catnip\n\t* Grass"""
''')

# 将转义序列和格式化字符串组合在一起
hw = "\aCR_test\r:\x68\145llo,\nworld"
print(f"test1{hw}")

print("test2{}".format("\aworld\bb2\\ hello"))