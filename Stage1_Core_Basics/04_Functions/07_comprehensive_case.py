money = 500000
def query():
    print("----------------查询余额----------------")

def deposit():
    print("------------------存款-----------------")
    num = int(input("输入您的存款金额："))
    global money
    money += num
    print(f"{name},您好，您存款{num}元成功")

def withdraw():
    print("------------------取款-----------------")
    num = int(input("输入您的取款金额："))
    global money
    money -= num
    print(f"{name},您好，您取款{num}元成功")

while True:
    name = input("欢迎来到银行ATM，请输入您的姓名：")
    while True:
        print("-----------------主菜单-----------------")
        print(f"{name}，您好，欢迎来到银行ATM,请选择操作：\n"
            f"查询余额\t[输入1]\n"
            f"存款\t\t[输入2]\n"
            f"取款\t\t[输入3]\n"
            f"退出\t\t[输入4]")
        option = int(input("请输入您的选择："))

        if option == 1:
            query()
        elif option ==2:
            deposit()
        elif option == 3:
            withdraw()
        else:
            print("程序退出\n")
            break

        print(f"{name},您好，您的余额剩余{money}\n")