# 打开不存在的文件
f = open("test.txt", "w", encoding="utf-8")

# write写入
f.write("Hello World!")     # 内容写入到内存中

# flush刷新
f.flush()       # 将内存中的内容写入硬盘

# close关闭
f.close()       # close方法内置了flush功能




# 打开已经存在的文件
f = open("test.txt", "w", encoding="utf-8")

# 写入并刷新
f.write("你好，IT")
f.close()