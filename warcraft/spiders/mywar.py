# -*- coding: utf-8 -*-
import scrapy
from warcraft.items import WarcraftItem
from bs4 import BeautifulSoup

class MywarSpider(scrapy.Spider):
    name = "myfilm"
    allowed_domains = ["www.douban.com"]
    start_urls = (
        'https://movie.douban.com/subject/25662329/comments',
    )
    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc)
        filename = response.url.split(".")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = WarcraftItem()
        item['title'] = soup.title.string
        item['comment'] = soup.find_all('p', class_="")
        return item
