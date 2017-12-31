#!/usr/bin env python3
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
	name = "article"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
				  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

def parse(self, response):
	item = Article()
	title = response.xpath('//h1/text()')[0].extract()
	print("Title is: " + title)
	item['title'] = title
	return item

##完善后的代码
from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpiderItem(CrawlSpider):
	name = "article"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
				  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
	rules = [Rule(SgmlLinkExtractor(allow = ('(/wiki/)((?!:).)*$'),),
				  callback="parse_item", follow=True)]

def parse_item(self, response):
	item = Article()
	title = response.xpath('//h1/text()')[0].extract()
	print("Title is: " + title)
	item['title'] = title
	return item

