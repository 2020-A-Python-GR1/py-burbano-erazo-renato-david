import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' #Heredado

    allowed_domains = [ #Heredado, dominios permitidos 
        'un.org' #para no salirse a dominios externos quedarse en la ONU
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    ##definir una tupla
    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' # Nombre de la función a ejecutar para parsear
        ),
        # segundo parámetro vacío
    )

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),
            callback ='parse_page'
        ),
        # Parámetro vacío
    )

    segmentos_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = segmentos_restringidos
            ),
            callback ='parse_page'
        ),
        # Parámetro vacío
    )
    
    rules = regla_tres # Heredada

    def parse_page(self, response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()
        #div.field-item > h4::text
        for agencia in lista_programas:
            with open('onu_agencias.text','a+', encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')
