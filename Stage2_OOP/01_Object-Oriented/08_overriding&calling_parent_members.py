class Phone:
    IMEI = None
    producer = "fanyunfei"

    def call_by_5g(self):
        print("使用5g通话")

# 复写
class MyPhone(Phone):
    producer = "fanbyteio"

    def call_by_5g(self):
        print("通话时使用cpu单核模式，节省电量")

        # # 调用父类成员-方法1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # # 调用父类成员-方法2
        # print(f"父类的厂商是：{super().producer}")
        # super().call_by_5g()

        print("关闭cpu单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)