# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LegendsItem(scrapy.Item):
    # 英雄名称
    name = scrapy.Field()
    # 英雄图片
    pic = scrapy.Field()
    # 英雄定位
    position = scrapy.Field()
    pass

class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
