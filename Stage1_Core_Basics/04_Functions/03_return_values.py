# 函数返回值的定义
def add(x,y):
    return x + y

r = add(13,14)
print(r)




# None类型

# 无return语句的函数返回值
def welcome():
    print("WELCOME TO HeiHan!")
result = welcome()
print(result)
print(type(result))

# 主动返回None
def welcome():
    print("WELCOME TO HeiHan!")
    return None
result = welcome()
print(result)
print(type(result))

# None用于if判断
def check_age(age):
    if age >= 18:
        return "Success"
    else:
        return None

result = check_age(17)
if not result:
    print("未成年禁止入内")

# None用于声明一些无初始内容的变量
