# 使用构造方法对成员变量进行赋值
class Student:
    # name = None
    # age = None
    # tel = None
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")

stu = Student("周杰伦", "20", "18066668888")
print(stu.name)
print(stu.age)
print(stu.tel)

# 练习案例
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

students = []
total_students = 10  # 把总数提取成一个变量，方便以后修改

for i in  range(total_students):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")

    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    new_student = Student(name, age, address)

    students.append(new_student)
    print(f" 学生 {i} 信息录入完成！【姓名：{new_student.name}，年龄：{new_student.age}，地址：{new_student.address}】")