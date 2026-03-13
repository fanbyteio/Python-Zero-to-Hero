# 通过下标索引取出元组中的元素
t1 = ((1, 2, 3), (4, 5, 6))
num = t1[1][2]
print(f"从元组中取出的元素是：{num}")

t2 = ("fanyunfei", 666, "dashuaibi", "youqianduojin")
# index查找方法
index = t2.index("fanyunfei")
print(f"元组t2中“fanyunfei”的下标是：{index}")

# count统计方法
t3 = ("fanyunfei", 666, "dashuaibi", "youqianduojin", "youqianduojin", "youqianduojin")
num = t3.count("youqianduojin")
print(f"元组t3中“youqianduojin”的数量有：{num}个")


num = len(t3)
print(f"元组t3中一共有{num}个元素")




# 元组的遍历
# while循环
index = 0

while index <len(t2):
    print(t2[index])
    index += 1

# for循环
print("t3的元素有：")
for element in t3:
    print(element)




# 元组的修改
t4 = ("fanyunfei", 1543, ["youqianduojin", "fanyunfei"])
print(f"t4的内容是：{t4}")
t4[2][0] = "fanyunfei"
t4[2][1] = "youqianduojin"
print(f"t4的内容是：{t4}")