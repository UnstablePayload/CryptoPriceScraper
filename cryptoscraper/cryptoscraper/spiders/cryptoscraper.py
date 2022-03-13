import scrapy

class CryptoSpider(scrapy.Spider):
    name = 'crypto'
    start_urls = ['https://crypto.com/price']

    def parse(self, response):
        for crypto in response.css('tr.css-17yof7g'):
            yield {
                'name': crypto.css('span.chakra-text.css-1mrk1dy::text').get(), 
                'price': crypto.css('div.css-b1ilzc::text').get(), 
                '24hChange': crypto.css('p.chakra-text::text').get(),
            }