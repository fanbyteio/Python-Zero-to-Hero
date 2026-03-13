print("欢迎来到黑马程序员！请出示您的健康码以及72小时核核酸证明，并配合测量体温！")
def judge(tem):
    if tem <= 37.5:
        print("体温测量中......")
        print(f"您的体温是：{tem}°，体温正常请进")
    else:
        print("体温测量中......")
        print(f"您的体温是：{tem}°，需要隔离！")

judge(float(input("输入你的体温")))