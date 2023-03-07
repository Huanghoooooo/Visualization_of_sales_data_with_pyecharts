'''
数据定义的类
'''


class Record:
    # 用构造方法的形式进行变量定义,可以很方便地进行成员变量的赋值
    def __init__(self, date, order_id, money, province):
        self.date = date  # 订单日期
        self.order_id = order_id  # 订单ID
        self.money = money  # 订单金额
        self.province = province  # 省份
