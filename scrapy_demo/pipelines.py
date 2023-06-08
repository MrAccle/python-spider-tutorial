# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TagPipeline:

    def open_spider(self, spider):
        self.file = open("./output/tag.json", "w")
        self.items = []

    def process_item(self, item, spider):
        print("process_item ->", item, spider)
        self.items.append(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        self.file.writelines(json.dumps(self.items))
        self.file.close()


class BookPipeline:
    def open_spider(self, spider):
        self.file = open("./output/book.json", "w")
        self.items = []

    def process_item(self, item, spider):
        print("process_item ->", item, spider)
        self.items.append(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        self.file.writelines(json.dumps(self.items))
        self.file.close()
