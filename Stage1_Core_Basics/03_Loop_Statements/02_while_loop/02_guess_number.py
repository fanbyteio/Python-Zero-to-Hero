import random
num = random.randint(1,100)
i = 1
guess = int(input("现有一个随机的1~100之间的数字\n请猜猜它是多少"))
while guess != num:
    if guess < num:
        print("你猜小了")
    else:
        print("你猜大了")
    guess = int(input("再猜一次"))
    i += 1
print(f"恭喜你，第{i}次猜对了！")