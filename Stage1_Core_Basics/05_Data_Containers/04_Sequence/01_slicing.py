# 对列表切片
my_list = [0, 1, 2, 3, 4, 5, 6]
print(f"结果1：{my_list[1:4]}")

# 对元组切片
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(f"结果2：{my_tuple[:]}")

# 对字符串切片
my_str= "0123456"
print(f"结果3：{my_str[::2]}")




# 对列表切片，步长为负数
print(f"结果4：{my_list[::-1]}")

# 对元组切片，步长为负数
print(f"结果4：{my_tuple[3:1:-1]}")

# 对字符串切片，步长为负数
print(f"结果4：{my_str[::-2]}")