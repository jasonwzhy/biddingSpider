import scrapy
class ChinaBiddingSpider(scrapy.Spider):
	name = "chinabidding"
	allow_domains = ["chinabidding.com"]
	# start_urls=[
	# 	"https://cas.ebnew.com/cas/login",
	# 	"http://www.chinabidding.com/search/proj.htm",
	#	"http://www.chinabidding.com/bid/index/loginIndex.htm"
	# ]
	def start_requests(self):
		return [scrapy.FormRequest("https://cas.ebnew.com/cas/login",
									formdata = {'username':'p131','password':'zp0611zp','authorize':'true',
									'loginUrl':'http://www.chinabidding.com/bid/index/loginIndex.htm',
									'service':'http://www.chinabidding.com/bid/login/login.htm',
									'realService':'http://211.151.182.227:8091'},
									callback = self.onlogin)]
	def parse(self,response):
		pass
	def onlogin(self,response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)