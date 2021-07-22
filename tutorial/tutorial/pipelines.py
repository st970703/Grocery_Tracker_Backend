# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        self.db = self.conn['my_groceries']
        # self.collection = self.db['paknsave_tb']

    def process_item(self, item, spider):
        self.db[spider.name + '_tb'].insert(dict(item))
        return item
