# 打开不存在的文件
f = open("test.txt", "a", encoding="utf-8")
f.write("黑马程序员")
f.flush()
f.close()

# 打开一个存在的文件
f = open("test.txt", "a", encoding="utf-8")
f.write("\n月薪10个w")
f.close()