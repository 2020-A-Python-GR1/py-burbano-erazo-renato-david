import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlFybeka(CrawlSpider):
    name = 'crawl_fybeka' #Heredado

    allowed_domains = [ #Heredado, dominios permitidos 
        'fybeca.com' #para no salirse a dominios externos quedarse en la ONU
    ]

    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25'
    ]

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains
                ##allow = segmentos_url_permitidos
            ),
            callback ='parse_page'
        ),
        # Parámetro vacío
    )
    
    rules = regla_tres # Heredada

    def parse_page(self, response):
        lista_productos = response.css('div.product-tile-inner > a.name::text').extract()
        print("Hola soy yo")
        #div.field-item > h4::text
        for producto in lista_productos:
            with open('fybeca_productos_belleza.text','a+', encoding='utf-8') as archivo:
                archivo.write(producto + '\n')
