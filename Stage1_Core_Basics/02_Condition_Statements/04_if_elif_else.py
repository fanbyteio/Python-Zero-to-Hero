# print("欢迎来到黑马动物园")
#
# if int(input("请输入你的身高（cm）:")) < 120:
#     print("你的身高小于120cm，可以免费游玩。")
# elif int(input("请输入你的VIP等级（1-5）：")) > 3:
#     print("你的VIP级别大于3，可以免费游玩。")
# elif int(input("请输入今天的日期（1-30）：")) == 1:
#     print("今天是1号免费日，可以免费游玩。")
# else:
#     print("不好意思，所有条件都不满足，需要购票10元。")
# print("祝您游玩愉快。")




# if_elif_else组合语句练习题
num = 10
if int(input("猜猜我心里的数字:")) == 10:
    print("恭喜你猜对了！")
elif int(input("不对，再猜一次：")) == 10:
    print("恭喜你猜对了！")
elif int(input("不对，再猜最后一次：")) == 10:
    print("恭喜你猜对了！")
else:
    print("Sorry，全部猜错了，我想的是10。")

