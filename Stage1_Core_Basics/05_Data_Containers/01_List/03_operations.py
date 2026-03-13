# 列表的常用操作

# 查询
my_list = ["fanyunfei", "dashuaibi", "youqianduojin"]
index = my_list.index("fanyunfei")
print(index)
# 如果查询不到会报错ValueError
# index = my_list.index("fanyufei")

# 修改
my_list[1] = "fengliutitang"
print(my_list)

# 插入
my_list.insert(1, "NB")
print(my_list)

# 追加单个元素
my_list.append('13949323982')
print(my_list)
# 批量追加
character = [175, 70]
my_list.extend(character)
print(my_list)

# 删除
# 通过下标删除——方法1
del my_list[6]
print(my_list)
# 通过下标删除——方法2
element = my_list.pop(5)    # 也可不接收返回值
print(f"取出的元素是{element}，列表：{my_list}")
# 通过内容删除
my_list = ["fanyunfei", "NB", "fanyunfei",  "fengliutitang", "youqianduojin", "13949323982"]
my_list.remove("fanyunfei")
print(my_list)

# 清空
my_list.clear()
print(my_list)

# 统计
# 统计某个元素在列表中的数量
my_list = [1, 1, 1, 2, 2, 2, 2, 3]
count = my_list.count(2)
print(f"2在列表中的个数是：{count}")
# 统计列表内一共有多少个元素
count = len(my_list)
print(f"列表中一共有{count}个元素")