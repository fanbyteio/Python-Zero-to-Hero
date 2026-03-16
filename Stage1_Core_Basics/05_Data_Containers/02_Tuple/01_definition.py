# 元组的定义
t1 = (1,"Helo",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是:{t1}")
print(f"t2的类型是：{type(t2)},内容是:{t2}")
print(f"t3的类型是：{type(t3)},内容是:{t3}")

# 定义单个元素的元组
t4 = ("fanyunfei")
print(f"t4的类型是：{type(t4)},内容是:{t4}")
t4 = ("fanyunfei",)
print(f"t4的类型是：{type(t4)},内容是:{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)},内容是:{t5}")

# 通过下标索引取出元组中的元素
num = t5[1][2]
print(f"从元组中取出的元素是：{num}")