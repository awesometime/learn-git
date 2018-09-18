# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-
import json

class TencentPipeline(object):
    """
       功能：保存item数据
    """
    def __init__(self):
        self.filename = open("G:\\PyCharm\\PythonProjects\\Tencent\\Tencent\\tencent.json", "w")

    def process_item(self, item, spider):
        # json.dumps()函数是将一个Python数据类型列表进行json格式的编码
        # json.dump() 将json信息写进文件
        # json.dumps()函数是将字典转化为字符串
        # json.load   读取文件中json信息
        # json.loads()函数是将字符串转化为字典
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"

        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()
