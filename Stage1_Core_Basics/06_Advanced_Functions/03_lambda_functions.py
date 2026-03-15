# 函数作为参数传递
def test_func(func):
    result = func(1, 2)
    print(f"func参数的类型是”：{func}")
    print(f"计算结果：{result}")


def compute(x, y):
    return x + y

test_func(compute)




# lambda匿名函数
def test_func(func):
    result = func(1, 2)
    print(f"计算结果：{result}")

test_func(lambda x, y : x + y)