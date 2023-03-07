'''
和文件相关的类定义
'''
import json

from data_define import Record  # 导包record是为类型注解用

# 先定义一个抽象类用来顶层设计，来确定哪些功能需要实现


class FileReader:
    def read_data(self) -> list[Record]:
        # 读取文件的数据，读取的每一条数据都转换为Record对象，将这些Record对象用list封装起来
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 利用构造函数，定义成员变量，（在调用read_data函数时自动）记录文件的路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []  # 创建一个list接受传入的数据
        for line in f.readlines():
            line = line.strip()  # 消除读取的数据中多出的换行符\n
            # print(line)
            data_list = line.split(",")  # 按逗号分割数据得到数据列表
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])  # 把封装好的数据变成类对象，顺序见FileReader类
            record_list.append(record)  # 将record追加写入到record_list中

        f.close()

        return record_list  # 返回数据列表


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            Record(data_dict["date"], data_dict["order_id"],int(data_dict["money"]),data_dict["province"])

        f.close()
        return record_list

# if __name__ == '__main__':
#     text_file_reader = TextFileReader(r"D:\CODE\testproject\test230307\test_pyecharts\2011年2月销售数据JSON.txt")
#     text_file_reader.read_data()
