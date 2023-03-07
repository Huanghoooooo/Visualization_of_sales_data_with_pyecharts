'''
1 设计一个类，可以完成数据的封装 data_define.py
2 设计一个抽象类，定义文件读取的相关功能，并使用子类方法实现具体功能 file_define.py
3 读取文件，生产数据额对象
4 进行数据需求的逻辑计算（计算每一天的销售额）
通过pyecharts进行图形绘制
'''


from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts import *
from pyecharts.globals import ThemeType


text_file_reader = TextFileReader(r"testproject\test230307\test_pyecharts\2011年1月销售数据.txt")
json_file_reader = JsonFileReader(r"D:\CODE\testproject\test230307\test_pyecharts\2011年2月销售数据JSON.txt")


data_1: list[Record] = text_file_reader.read_data()
data_2: list[Record] = json_file_reader.read_data()
# 将两份data数据合并为一个list来存储
all_data: list[Record] = data_1 + data_2

# 开始进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():  # keys对应日期，而values则是金额总和
        # 当前日期已经有记录了，则和老记录累加即可
        data_dict[record.date] += record.money
    else:
        # 当前日期没有记录，则创一个新的日期记录
        data_dict[record.date] = record.money


bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()),label_opts=options.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=options.TitleOpts(title="每日销量")
)
bar.render(r"D:\CODE\testproject\test230307\test_pyecharts\可视化.html")
