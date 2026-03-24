# 捕获常规异常
try:
    f = open("ubuntu.txt", "r", encoding="utf-8")
except:
    print("文件不存在，改为w模式打开文档")
    f = open("ubuntu.txt", "w", encoding="utf-8")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print(e)

# 捕获多个异常
try:
    1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print(e)

# 捕获所有异常
try:
    1 / 0
    print(name)
    f = open("ubuntu.txt", "r", encoding="utf-8")
except Exception as e:
    print('出现异常了')
    print(e)

# 异常else
try:
    print('Hello World!')
except Exception as e:
    print('出现异常了')
    print(e)
else:
    print('无异常')

# 异常finally
try:
    print('Hello World!')
    print(name)
except Exception as e:
    print('出现异常了')
    print(e)
else:
    print('无异常')
finally:
    print('无论有没有异常都会输出')