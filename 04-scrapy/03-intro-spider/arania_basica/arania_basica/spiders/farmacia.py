import scrapy

class FarmaciaSpider(scrapy.Spider):
    name = 'farmacia_spider'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in urls:
            yield scrapy.Requests(url=url)

    def parse(self,response): ##parsean las cosas
        etiqueta_contendedora = response.css(
            'div.product-tile-inner > div > div.side > div.price::text'
        ).extract()
        
        

# scrapy crawl nombre_arania