# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi_1(self):
        print(f"大家好，我是{self.name},请大家多多关照")

    def say_hi_2(self, msg):
        print(f"大家好，我是{self.name},{msg}")

stu1 = Student()
stu1.name = "周杰伦"
stu1.say_hi_1()
stu1.say_hi_2("哎呦，不错哦")

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi_1()
stu2.say_hi_2("我看好你哦")