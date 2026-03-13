age = int(input("请输入你的年龄："))
year = int(input("请输入你的入职时间："))
level = int(input("请输入你的级别："))

if age >= 18:
    print("你确实是成年人")
    if age < 30:
        print("你满足了年龄条件")
        if year > 2:
            print("你的年龄和入职时间达标，可以领取奖励")
        elif level > 3:
            print("你的年龄和级别达标，可以领取奖励")
        else:
            print("你的入职时间和级别都不达标，无法领取奖励")
    else:
        print("你的年龄过大，无法领取奖励")
else:
    print("你是未成年，无法领取奖励")




# 判断语句综合案例(自写版)
import random
num = random.randint(1,10)
guess = int(input("现在随机生成了一个1~10之间的数字，你有三次机会猜中这个数字："))
if  guess< num:
    guess = int(input("小了，再猜:"))
    if guess < num:
        guess = int(input("小了，再猜"))
        if guess != num:
            print("不好意思吗，没有猜对")
        else:
            print("恭喜你猜对了！")

    elif guess > num:
        guess = int(input("大了，再猜:"))
        if guess != num:
            print("不好意思吗，没有猜对")
        else:
            print("恭喜你猜对了！")
    else:
        print("恭喜你猜对了！")
elif guess > num:
    guess = int(input("大了，再猜:"))
    if guess < num:
        guess = int(input("小了，再猜"))
        if guess != num:
            print("不好意思吗，没有猜对")
        else:
            print("恭喜你猜对了！")

    elif guess > num:
        guess = int(input("大了，再猜:"))
        if guess != num:
            print("不好意思，没有猜对")
        else:
            print("恭喜你猜对了！")
    else:
        print("恭喜你猜对了！")
else:
    print("恭喜你猜对了！")




# 判断语句综合案例(老师版)
import random
num = random.randint(1,10)
guess = int(input("现在随机生成了一个1~10之间的数字，你有三次机会猜中这个数字："))

if guess == num:
    print("恭喜你第一次就猜对了！")
else:
    if guess < num:
        print("猜小了")
    else:
        print("猜大了")

    guess = int(input("再猜一次"))

    if guess == num:
        print("恭喜你第二次猜对了！")
    else:
        if guess < num:
            print("猜小了")
        else:
            print("猜大了")

        guess = int(input("再猜一次"))

        if guess == num:
            print("恭喜你最后一次猜对了！")
        else:
            print("不好意思，没有猜对")


