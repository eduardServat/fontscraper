import scrapy

from fontscraper.items import FontscraperItem


class FontsquirrelSpider(scrapy.Spider):
    name = 'fontsquirrel'
    allowed_domains = ['fontsquirrel.com']
    start_urls = ['http://fontsquirrel.com/']

    def start_requests(self):
        return [
            scrapy.Request(
                url='https://www.fontsquirrel.com/fonts/list/find_fonts?filter%5Bdownload%5D=local',
                callback=self.parse
            ),
        ]

    def parse(self, response):
        next_url = response.xpath('//*[@id="main_content"]/div/div[1]/div[5]/a[@rel="next"]/@href').extract_first()
        file_urls = response.xpath('//*[@id="font_list"]//div/div/span[1]/div/span[2]/a/@href').extract()
        file_urls = [response.urljoin(url) for url in file_urls]
        item = FontscraperItem()
        item['file_urls'] = file_urls
        yield item
        if next_url:
            self.logger.info('Next page: %s ' % next_url)
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)
