f1 = open("bill.txt", "r", encoding="utf-8")
f2 = open("bill.txt.bak", "w", encoding="utf-8")
for line in f1:
    line_list = line.replace("\n", "").split(",")
    if line_list[-1] == "正式":
        f2.write(line)

f1.close()
f2.close()