import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    start_urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in start_urls:
            yield scrapy.Requests(url=url)

    def parse(self,response): ##parsean las cosas
        etiqueta_contendedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        imagenes = etiqueta_contendedora.css(
            'div.image_container > a > img::attr(src)'
        )
        stock = etiqueta_contendedora.css(
            'div.product_price > p.availability'
        )
        precios = etiqueta_contendedora.css(
            'div.product_price > p.price_color::text'
        )



        print(titulos)
        print(imagenes)
        print(stock)
        print(precios)

# scrapy crawl nombre_arania