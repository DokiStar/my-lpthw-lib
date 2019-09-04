# 定义一个字符串型变量formatter，其值为“{} {} {} {}”，其中“{}”为通配符，一组{}对应一个内嵌的变量
formatter = "{} {} {} {}"

# 输出内嵌整数1、2、3和4的变量formatter
print(formatter.format(1, 2, 3, 4))
# 输出内嵌字符串“one”、“two”、“three”和“four”的formatter
print(formatter.format("one", "two", "three", "four"))
# 输出内嵌布尔值的formatter
print(formatter.format(True, False, True, False))
# 输出变量formatter内嵌自己的字符串，结果为16组“{}”
print(formatter.format(formatter, formatter, formatter, formatter))
# 输出四个字符串拼接而成的新字符串，结果为：是谁？ 帮我收了 白色的 数据线
print(formatter.format(
    "是谁？",
    "帮我收了",
    "白色的",
    "数据线"
))
