from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class MySpider(RedisCrawlSpider):
    name = 'myspider'
    max_idle_time = 2
    redis_key = 'dcrawl:urls'

    allowed_domains = ["coindesk.com"]

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def parse_item(self, response):

        yield {
            'url': response.url
        }
