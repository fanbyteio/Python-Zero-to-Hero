# 使用while循环遍历列表
def list_while_func():
    my_list = ["fanyunfei", "youqianduojin", "fengliutitang"]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

list_while_func()

def list_for_func():
    my_list = [1, 2, 3, 4, 5, 6]
    for element in my_list:
        print(element)

list_for_func()

# 遍历列表练习案例——while循环
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
even_list = []
while index < len(my_list):
    if my_list[index] % 2 == 0:
        even_list.append(my_list[index])
    index += 1
print(f"偶数列表是：{even_list}")

# 遍历列表练习案例——for循环
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for element in my_list:
    if element % 2 == 0:
        even_list.append(element)
print(f"偶数列表是：{even_list}")
