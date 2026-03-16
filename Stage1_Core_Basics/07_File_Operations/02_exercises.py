num = 0
with open("word.txt", "r", encoding="utf-8") as f:
    for line in f:
        num += line.count("itheima")
print(num)