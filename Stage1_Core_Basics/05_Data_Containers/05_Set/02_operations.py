# 添加新元素
my_set = {"fanyunfei", "youqianduojin", "dashuaibi"}
my_set.add("pingbuqingyun")
print(f"添加后的集合是：{my_set}")

# 移除元素
my_set.remove("pingbuqingyun")
print(f"移除后的集合是：{my_set}")

# 随机取出元素
element= my_set.pop()
print(f"随机取出的元素是{element}，取出后的集合是：{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空后是：{my_set}")

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set1, set2, set3)

# 消除交集
set1.difference_update(set2)
print(set1, set2)

# 取并集
set1 = {1, 2, 3}
set3 = set1.union(set2)
print(set1, set2, set3)

# 统计集合元素数量
num = len(set1)
print(num)

# 集合的遍历
# 集合不支持下标索引，因此不能使用while遍历
for item in set3:
    print(item)