# index索引方法
str1 = "fanyunfei youqianduojin"
value = str1.index("youqianduojin")
print(value)

# replace替换方法
str2 = str1.replace("youqianduojin","有钱多金")
print(f"将字符串str1：{str1}替换后得到str2：{str2}")

# split分割方法
str1 = "fanyunfei is a dashuaibi"
str1_list = str1.split(" ")
print(f"将字符串str1：{str1}按照空格分割后得到的列表是：{str1_list},类型是{type(str1_list)}")

# strip规整方法
str1 = "  1543fanyunfei is a dashuaibi3451  "
new_str1 = str1.strip()     # 不传入参数，默认去除前后空格
new_str2 = new_str1.strip("1543")
print(f"{str1}去除前后的空格后是：{new_str1}，去除前后的1543后是：{new_str2}")

# count统计方法
count = str1.count("f")
print(f"str1字符串中一共出现了{count}次f")

# len统计方法
num = len(str1)
print(f"str1中一共有{num}个字符")

# 字符串遍历
# while循环遍历
index = 0
while index < len(str1):
    print(str1[index])
    index += 1

# for循环遍历
for char in str1:
    print(char)