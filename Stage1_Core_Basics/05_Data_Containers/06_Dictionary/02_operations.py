# 新增元素
my_dict = {"周杰伦" : 99, "林俊杰" : 88, "张学友" : 77}
my_dict["张信哲"] = 66
print(my_dict)

# 更新元素
my_dict["周杰伦"] = 33
print(my_dict)

# 删除元素
score = my_dict.pop("周杰伦")
print(score, "\n",my_dict)

# 清空元素
my_dict.clear()
print(my_dict)

# 获取全部key
my_dict = {"周杰伦" : 99, "林俊杰" : 88, "张学友" : 77}
keys = my_dict.keys()
print(keys)

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
index = 1
for key in keys:
    print(f"key{index}:{key}")
    print(f"value{index}:{my_dict[key]}")
    index += 1

# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"方法2key:{key}")
    print(f"方法2value:{my_dict[key]}")

# 统计元素数量
num = len(my_dict)
print(num)
