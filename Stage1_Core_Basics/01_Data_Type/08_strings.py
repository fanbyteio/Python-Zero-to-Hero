# （1）字符串的三种定义方式
name_single = 'fanyunfei'
print(type(name_single),name_single)

name_double = "fanyunfei"
print(type(name_double),name_double)

name_triple = """fanyunfei"""
print(type(name_triple),name_triple)

# 引号嵌套
name = '"fanyunfei"'
print(name)
name = "'fanyunfei'"
print(name)
name = "\'fanyunfei\'"
print(name)
name = '\"fanyunfei\"'
print(name)
name = "\"\"fanyunfei\"\""
print(name)




# （2）字符串的拼接
print("fanyunfei"+"英俊潇洒风流倜傥有钱多金智商高")

name = "fanyunfei"
university = "ECNU"
tel = 13949323982
Email = "gisfanyunfei@gmail.com"

print("我的名字是" + name + "，目前就读于" + university + "，邮箱是" + Email + "，电话是" + str(tel))




# （3）字符串格式化
name = "传智播客"
set_up_year = 2026
stock_price = 19.99
print("%s成立于%d年，今天的股价是%f" %(name,set_up_year,stock_price))




# （4）字符串格式化的精度控制
num1 = 12
num2 = 12.3456
print("数字12宽度限制4，结果是：%4d" %num1)
print("数字12宽度限制1，结果是：%1d" %num1)
print("数字12.34宽度限制7，小数精度3，结果是：%7.3f" %num2)
print("数字12.34宽度限制10，小数精度6，结果是：%10.6f" %num2)




# （5）快速字符串格式化
name = "传智播客"
set_up_year = 2026
stock_price = 19.99
print(f"{name}成立于{set_up_year}年，今天的股价是{stock_price}")




# （6）对表达式进行格式化
print("1 + 1的结果是：%d" %(1 + 1))
print(f"1 + 1的结果是：{1 +1}")
print("字符串在python中的类型是：%s" %type("fanyunfei"))




# （7）字符串格式化课后练习
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过 %d 天的增长后，股价达到了：%.2f" %(stock_price_daily_growth_factor,growth_days,stock_price*(stock_price_daily_growth_factor**growth_days)))