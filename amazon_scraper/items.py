# amazon_scraper/items.py

import scrapy

class AmazonScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
