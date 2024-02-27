from trending.sites.HimalayanTimes import himalayan_times
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import signals

def run_scrapy():
    crawler = Crawler(himalayan_times,settings={})
    crawler.signals.connect(reactor.stop,signal=signals.spider_closed)
    extra_spiders_args = {}
    crawler.crawl(**extra_spiders_args)