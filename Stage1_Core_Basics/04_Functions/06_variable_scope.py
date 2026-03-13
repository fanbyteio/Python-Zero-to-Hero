# 局部变量演示
def test_a():
    num = 100
    print(num)

test_a()
# print(num)   # 局部变量无法在函数外部使用




# 全局变量演示
num = 200
def test_a():
    print(f"tets_a:{num}")

def test_b():
    print(f"tets_b:{num}")

test_a()
test_b()
print(num)




# 函数内部无法修改全局变量
num = 100
def test_a():
    num = 200
    print(num)

test_a()
print(num)




# global声明函数内变量为全局变量
num = 100
def test_a():
    global num
    num = 200
    print(num)

test_a()
print(num)
