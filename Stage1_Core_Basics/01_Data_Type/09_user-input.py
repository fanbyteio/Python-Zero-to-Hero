name = input("请告诉我你的名字")
print(f"你的名字是：{name}")

tel = input("请告诉我的你的电话号码")
print(f"你的电话号码是：{tel}")
print(f"input读取到的数据类型是：{type(tel)}")
tel = int(tel)
print(f"手动转为int类型：{type(tel)}")




# 数据输入的练习
user_name = input("请输入您的名称")
user_type = input("请输入用户类型")
print(f"您好：{user_name}，您是尊贵的{user_type}用户，欢迎您的光临。")
