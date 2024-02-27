import scrapy
import random
from amazon_scraper.items import AmazonScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?k=python+books',
        'https://www.amazon.com/s?k=big+data+books',
        'https://www.amazon.com/s?k=data+analytics+books'
    ]

    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        # Add more User-Agents as needed
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 5,  # Adjust the delay as needed
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': random.choice(self.user_agents)})

    def parse(self, response):
        products = response.xpath('//div[@data-asin]')

        for product in products:
            item = AmazonScraperItem()
            item['title'] = product.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get()
            item['author'] = product.xpath('.//a[@class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style"]/text()').get()
            item['price'] = product.xpath('.//span[@class="a-price"]/span[@class="a-offscreen"]/text()').get()
            item['rating'] = product.xpath('.//span[@class="a-icon-alt"]/text()').get()
            item['url'] = response.urljoin(product.xpath('.//@href').get())

            author_link = item['url']
            yield scrapy.Request(url=author_link, callback=self.parse_author, meta={'item': item.copy()})

        # Follow pagination links
        next_page = response.css('li.a-last a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_author(self, response):
        item = response.meta['item']
        # Do not extract the description field
        yield item
