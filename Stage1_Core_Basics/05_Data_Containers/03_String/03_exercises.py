str1 = "itheima itcast boxuegu"
print(f"字符串{str1}中有{str1.count("it")}个it字符")
str2 = str1.replace(" ","|")
print(f"字符串{str1}被替换空格后的结果是{str2}")
print(f"字符串{str2}按照|分隔后，得到{str2.split("|")}")