import json

import scrapy
from bs4 import BeautifulSoup

from scrapy_demo.items import BookItem


class BookSpider(scrapy.Spider):
    name = "bookSpider"
    allowed_domains = ["book.douban.com"]
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {"scrapy_demo.pipelines.BookPipeline": 300},
    }

    def parse(self, response):
        print("ready to parse the book ---------------> ", response.body)
        soup = BeautifulSoup(response.body, 'html.parser')
        for td in soup.find("div", id="subject_list").find_all("li"):
            book = BookItem()
            info = td.find("div", class_="info")
            book["name"] = info.find("a").get("title")
            book["publish"] = info.find("div", class_="pub").text.strip()
            book["score"] = info.find("span", class_="rating_nums").text
            book["introduction"] = info.find("p").text.strip()
            book["href"] = td.find("a", class_="nbg").get("href")
            book["pic"] = td.find("img").get("src")
            yield book

    def start_requests(self):
        # 由于是通过run来执行，因此从run.py做相对目录
        f = open("./output/tag.json", "r", encoding="utf-8")
        # tags
        tags = json.loads(f.read(-1))
        for tag in tags:
            print("yield the tag", tag)
            # 每种类型爬取60个
            for i in range(1):
                yield scrapy.Request(url="https://book.douban.com" + tag["url"] + "?type=T&start=" + str(i * 20),
                                     callback=self.parse)
        f.close()


if __name__ == '__main__':
    # f = open("../output/tag.json", "r", encoding="utf-8")
    # print(f)
    # f.close()

    # 测试提取元素
    f = open("../source/book.html", "r", encoding="utf-8")
    body = f.read(-1)
    soup = BeautifulSoup(body, 'html.parser')
    for td in soup.find("div", id="subject_list").find_all("li"):
        info = td.find("div", class_="info")
        print({
            "name": info.find("a").get("title"),
            "publish": info.find("div", class_="pub").text.strip(),
            "score": info.find("span", class_="rating_nums").text,
            "introduction": info.find("p").text.strip(),
            "pic": td.find("a", class_="nbg").get("href")
        })
        # item = td.find("a")
