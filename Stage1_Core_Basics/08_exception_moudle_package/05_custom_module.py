# # import 导入自定义模块
# import my_module
# my_module.test(1 , 2)
#
# # from导入自定义模块
# from my_module import test
# test(2, 3)




# 命名空间污染--当导入多个模块且使用了同名功能时，调用的是后导入模块的功能
# from my_module1 import test
# from my_module2 import test
# test(1,2)




# __main__变量
import my_module1
from my_module1 import test

from my_module1 import *
test_a()
# test_b()    # test_b在这里无法使用