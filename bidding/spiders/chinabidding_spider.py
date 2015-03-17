import scrapy
class ChinaBiddingSpider(scrapy.Spider):
	name = "chinabidding"
	allow_domains = ["chinabidding.com"]
	start_urls=[
		"https://cas.ebnew.com/cas/login",
		"http://www.chinabidding.com/search/proj.htm"
	]
	def start_requests(self):
		return [scrapy.FormRequest("https://cas.ebnew.com/cas/login",
									formdata = {'username':'p131','password':'zp0611zp'},
									callback = self.onlogin)]
	def parse(self,response):
		pass
	def onlogin(self,response):
		pass