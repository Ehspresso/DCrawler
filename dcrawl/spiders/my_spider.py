from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class MySpider(RedisCrawlSpider):
    name = 'myspider'
    redis_key = 'myspider:start_urls'
    max_idle_time = 2

    start_urls = ['https://coindesk.com']
    allowed_domains = ["coindesk.com"]

    num_crawled = 0

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        self.num_crawled += 1

        yield {
            'url': response.url
        }

        self.logger.info(f'{self.num_crawled}\n')

        if self.num_crawled == 6000:
            raise CloseSpider('Max crawls reached!')