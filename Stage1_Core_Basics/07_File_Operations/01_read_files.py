import time

# 打开文件
# f = open("D:/Code/PycharmProject/python_learning/Stage1_Core_Basics/07_File_Operations/测试.txt", "r", encoding = "utf - 8")
f = open("测试.txt", "r", encoding = "UTF-8")
print(type(f))

# 读取文件 - read
print(f"读取10个字符：{f.read(10)}")
print(f"读取全部内容：{f.read()}")
print("-------------------------------------------")

# 读取文件 - readlines()
lines = f.readlines()   # 读取文件的全部行，封装在列表中
print(f"lines对象的类型是{type(lines)}")
print(f"lines对象的内容是{lines}")

# 读取文件 - readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行内容是：{line1}")
print(f"第二行内容是：{line2}")
print(f"第三行内容是：{line3}")

# 读取文件 - for循环
for line in f:
    print(line)
time.sleep(30000)

# 文件的关闭
f.close()

# with open语法操作文件
with open("测试.txt", "r", encoding = "UTF-8") as f:
    for line in f:
        print(line)
