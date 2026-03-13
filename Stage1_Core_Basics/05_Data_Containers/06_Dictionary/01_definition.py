# 定义字典
my_dict1 = {"fanyunfei": 666, "youqianduojin" : 111}
my_dict2 = {}
my_dict3 = dict()

print(f"my_dict1: {my_dict1},type: {type(my_dict1)}")
print(f"my_dict2: {my_dict2},type: {type(my_dict2)}")
print(f"my_dict3: {my_dict3},type: {type(my_dict3)}")

# 从字典中基于key获得value
print(f"fanyunfei:{my_dict1["fanyunfei"]}")




# 定义嵌套字符串
stu_score_dict = {
    "樊云飞":{
        "语文":140, "数学":150, "英语":150
    },
    "分页符":{
        "语文":150, "数学":150, "英语":150
    },
    "慕砚舟":{
        "语文":150, "数学":150, "英语":149
    }
}

print(f"樊云飞的语文成绩：{stu_score_dict["樊云飞"]["语文"]}")
print(f"分页符的数学成绩：{stu_score_dict["分页符"]["数学"]}")
print(f"慕砚舟的英语成绩：{stu_score_dict["慕砚舟"]["英语"]}")