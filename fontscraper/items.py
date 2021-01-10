import scrapy


class FontscraperItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field
