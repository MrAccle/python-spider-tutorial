# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TagItem(scrapy.Item):
    # 标签名称
    name = scrapy.Field()
    # 标签url
    url = scrapy.Field()


class BookItem(scrapy.Item):
    # 书籍名称
    name = scrapy.Field()
    # 出版社
    publish = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 链接
    href = scrapy.Field()
