# __str__字符串魔术方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student类对象：name：{self.name}，age:{self.age}"

stu = Student("周杰伦", 31)
print(stu)
print(str(stu))

# __lt__小于魔术方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

stu1 = Student("周杰伦", 11)
stu2 = Student("林俊杰", 13)
print(stu1 < stu2)
print(stu1 > stu2)

# __le__小于等于魔术方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age


stu1 = Student("周杰伦", 11)
stu2 = Student("林俊杰", 13)
print(stu1 <= stu2)  # 结果:True
print(stu1 >= stu2)  # 结果:False

# __eq__比较运算发魔术方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周杰伦", 12)
stu2 = Student("林俊杰", 11)
print(stu1 == stu2)  # 结果:True
