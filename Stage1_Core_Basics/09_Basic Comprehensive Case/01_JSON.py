# 导入json模块
import json

# 列表转换为json
data = [{"name":"张三", "age":18}, {"name":"李四", "age":19}, {"name":"王五","age":20}]
data_str = json.dumps(data,ensure_ascii=False)
print(f"json_str的类型是：{type(data_str)}")
print(f"json_str的内容是：{data_str}")

# 字典转换为json
zjl = {"name":"周杰伦", "addr":"台北"}
zjl_str = json.dumps(zjl,ensure_ascii=False)
print(f"zjl的类型是：{type(zjl_str)}")
print(f"zjl的内容是：{zjl_str}")




# json转换为python数据类型-列表
data_str = '[{"name":"张三", "age":18}, {"name":"李四", "age":19}, {"name":"王五","age":20}]'
data = json.loads(data_str)
print(f"data_str的类型是：{type(data)}")
print(f"data_str的内容是：{data}")

# json转换为python数据类型-字典
zjl_str = '{"name": "周杰伦", "addr": "台北"}'
zjl = json.loads(zjl_str)
print(f"data_str的类型是：{type(zjl)}")
print(f"data_str的内容是：{zjl}")