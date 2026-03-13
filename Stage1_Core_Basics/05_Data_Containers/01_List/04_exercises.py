age_list = [21, 25, 21, 23, 22, 20]
age_list.append(31)
age_list.extend([29, 33, 30])
first = age_list.pop(0)
last = age_list.pop(-1)
index = age_list.index(31)
print(f"元素31的下标是：{index}")