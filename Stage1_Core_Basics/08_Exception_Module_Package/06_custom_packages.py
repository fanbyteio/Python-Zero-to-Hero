# import导入自定义的包中的模块并使用
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()




# from导入自定义的包中的模块并使用
from my_package import my_module1
from my_package import my_module2

my_module1.info_print1()
my_module2.info_print2()




# 直接导入模块中的功能
from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2

info_print1()
info_print2()



# 通过__all__变量，控制import
from my_package import *

my_module1.info_print1()
# my_module2.info_print2()        # 此时，info_print2不可使用
