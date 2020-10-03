import scrapy 
import pandas as pd
import numpy as np


class AraniaCrawlMetacritic2019(scrapy.Spider):
    name = 'metacritic_2019'

    allowed_domains = [
        'www.metacritic.com'
    ]

    urls = [
        'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2019&distribution=&sort=desc&view=detailed'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):

        titulo =  response.css('td.clamp-summary-wrap a.title h3::text').extract()
        plataforma = response.css('div.platform span.data::text').extract()
        fecha = response.css('div.clamp-details span::text').extract()
        metaScore = response.css('div.clamp-metascore a.metascore_anchor div.metascore_w::text').extract()
        userScore = response.css('div.clamp-userscore a.metascore_anchor div.user::text').extract()


        plataforma = AraniaCrawlMetacritic2019.transformar_plat(plataforma)
        fecha = AraniaCrawlMetacritic2019.transformar_fech(fecha)
        datos = {
            'Titulos' : titulo,
            'Plataforma' : plataforma,
            'Fecha' : fecha,
            'MetaScore' : metaScore,
            'UserScore' : userScore
        }

        data_frame = pd.DataFrame(datos)
        data_frame.to_csv('data_scrapy_2019.csv')
    
    @staticmethod
    def transformar_plat(plataformas):

        plats = []

        for plataforma in plataformas:
            plats.append(plataforma.replace("\n","").replace(" ",""))
        return plats

    @staticmethod
    def transformar_fech(fechas):
        fech = []
        for fecha in range(2, len(fechas),3):
            fech.append(fechas[fecha])

        return fech
        