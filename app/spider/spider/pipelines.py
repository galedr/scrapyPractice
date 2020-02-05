# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class StocksPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='mysql',
            db='scrapy_practice',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if item['code'] and item['name']:
            try:
                self.cursor.execute("SELECT * FROM stock WHERE code = %s", item['code'])
                ret = self.cursor.fetchone()
                if not ret:
                    self.cursor.execute("INSERT INTO stock (code, name) VALUES (%s, %s)", (item['code'], item['name']))
                    self.conn.commit()
            except Exception as e:
                self.conn.rollback()

        return item
