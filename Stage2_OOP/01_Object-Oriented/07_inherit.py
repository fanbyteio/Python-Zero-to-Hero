#单继承
# 父类
class Phone:
    producer = "fanbyteio"
    IMEI = None

    def call_by_4g(self):
        print("4g通话")

# 子类
class Phone2026(Phone):
    face_id = "000001"

    def call_by_5g(self):
        print("2026年新功能5g通话")

# 实例化
phone = Phone2026()

# 虽然Phone2026中没有这些变量和方法，但是Phone2026继承了Phone，可以使用Phone中有的变量和方法
print({phone.producer})
phone.call_by_4g()




# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "fanbyteio"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class myphone(Phone, NFCReader, RemoteControl):
    pass

phone = myphone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()


