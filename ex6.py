# 定义（整型）变量type_of_people，人的类型数量，值为10
types_of_people = 10
# 定义（字符串型）变量x，将变量types_of_people嵌入x
x = f"There are {types_of_people} types of people." # 第一处

# 定义（字符串型）变量binary，值为binary，变量名和值相同
binary = "binary"
# 定义（字符串型）变量do_not，值为don't，变量名和值不同
do_not = "don't"
# 定义（字符串型）变量y，将变量binary和do_not嵌入y
y = f"Those who know {binary} and those who {do_not}." # 第二处

# 输出字符串x
print(x)
# 输出字符串y
print(y)

# 输出一个内嵌x的字符串
print(f"I said: {x}") # 第三处
# 输出一个内嵌y的字符串
print(f"I also said: '{y}''") # 第四处

# 定义（布尔型）变量hilarious，值为False（假）
hilarious = False # 若要使其为真，可赋值True
# 定义（字符串型）变量joke_evaluation，内嵌其他变量（使用大括号）
joke_evaluation = "Isn't that joke so funny?! {}"

# 输出字符串joke_evaluation，其中joke_evaluation内嵌变量hilarious
print(joke_evaluation.format(hilarious)) # 第五处

# 定义字符串型变量w，表示字符串左侧
w = "This is the left side of..."
# 定义字符串型变量e，表示字符串右侧
e = "a string with a right side"

# 拼接字符串w和e（符号“+”运算符重载，实现拼接功能）
print(w + e)
