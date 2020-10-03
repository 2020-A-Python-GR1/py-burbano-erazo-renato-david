import scrapy
import pandas as pd
import numpy as np
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlMetacritic2019(CrawlSpider):
    name = 'def_meta'

    allowed_domains = [
        'www.metacritic.com' #para no salirse a dominios externos quedarse en la ONU
    ]

    start_urls = [
        'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2020&distribution=&sort=desc&view=condensed'
    ]

    segmentos_url_permitidos = (
        'browse/games/score/metascore/year/all/filtered?year_selected=2020&distribution=&sort=desc&view=condensed(.*?)',
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),
            callback ='parse_page'
        ),
    )
   
    rules = regla_dos

    def parse_page(self, response):

        titulos =  response.css('td.clamp-summary-wrap a.title h3::text').extract()
        plataforma = response.css('div.platform span.data::text').extract()
        fecha = response.css('div.clamp-details span::text').extract()
        metaScore = response.css('div.clamp-metascore a.metascore_anchor div.metascore_w::text').extract()
        userScore = response.css('div.clamp-userscore a.metascore_anchor div.user::text').extract()


        plataforma = AraniaCrawlMetacritic2019.transformar_plat(plataforma)
        fecha = AraniaCrawlMetacritic2019.transformar_fech(fecha)
        userScore = AraniaCrawlMetacritic2019.transformar_userScore(userScore)
        
        datos = {
            'Titulos' : titulos,
            'Plataforma' : plataforma,
            'Fecha' : fecha,
            'MetaScore' : metaScore,
            'UserScore' : userScore
        }

        for titulo in titulos:
            with open('titulo.text','a+', encoding='utf-8') as archivo:
                archivo.write(titulo + '\n')
        #data_frame = pd.DataFrame(datos)
        #data_frame.to_csv('def.csv')
    
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

    @staticmethod
    def transformar_userScore(userScores):
        scores = []
        for score in userScores:
            if(score == 'tbd'):
                score = 0
            scores.append(score)
        return scores
        

