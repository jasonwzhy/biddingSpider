import scrapy
class ChinaBiddingSpider(scrapy.Spider):
	name = "chinabidding"
	allow_domains = ["chinabidding.com"]
	start_urls=[
		"http://www.chinabidding.com/search/proj.htm"
	]
	def parse(self,response):
		pass