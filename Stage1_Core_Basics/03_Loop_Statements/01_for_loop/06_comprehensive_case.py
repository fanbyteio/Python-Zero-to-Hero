import random
salary = 10000
for i in range(1, 21):
    if salary <= 0:
        print("工资发完了，下个月领取吧")
        break
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位。")
        continue
    salary -= 1000
    print(f"向员工{i}发放工资1000元，账户余额{salary}元")



import random
salary = 10000
for i in range(1,21):
    if salary > 0:
        num = random.randint(1,10)
        if num < 5:
            print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位。")
            continue
        salary -= 1000
        print(f"向员工{i}发放工资1000元，账户余额{salary}元")
    else:
        print("工资发完了，下个月领取吧")
        break