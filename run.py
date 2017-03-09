from tutorial import spiders

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Closing reactor", level=log.INFO)
    reactor.stop()

log.msg(loglevel=log.DEBUG)
settings = Settings()

# crawl responsibly
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
crawler = CrawlerProcess(settings)

# stop reactor when spider closes
crawler.signals.connect(spider_closing)

crawler.configure()
crawler.crawl(spiders())
crawler.start()
reactor.run()