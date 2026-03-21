# 异常的传递
def func01():
    print("func01开始")
    num = 1 / 0
    print("func01结束")

def func02():
    print("func02开始")
    func01()
    print("func02结束")

def main():
    try:
        func02()
    except Exception as e:
        print(f"出现异常，异常信息：{e}")

main()