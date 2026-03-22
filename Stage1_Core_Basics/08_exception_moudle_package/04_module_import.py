# 通过import导入time模块使用sleep功能
import time

print(f"你好")
time.sleep(5)
print(f"我好")




# 通过from导入time模块中的sleep功能
from time import sleep
print(f"你好")
sleep(5)
print(f"我好")




# 使用 # 导入time的全部功能
from time import *
print(f"你好")
sleep(5)
print(f"我好")




# 使用as给模块加上别名
import time as t
print(f"你好")
t.sleep(5)
print(f"我好")




# 使用as给功能加上别名
from time import sleep as sl
print(f"你好")
sl(5)
print(f"我好")