import json
import parser
import csv


def return_informations(html_baixado):

    numero_likes = parser.parser(html_baixado, 'tooltip":"', "\"}}", True)
    numero_likes = numero_likes.split(' / ')

    dados = {'nome_do_vídeo': parser.parser(html_baixado, 'title":"', '","', False),
             'autor': parser.parser(html_baixado, '","author":"', '",', False),
             'likes': numero_likes[0],
             'deslikes': numero_likes[1],
             'visualização': parser.parser(html_baixado, 'viewCount":"', '",', True),
             'duração_do_video': parser.parser(html_baixado, '"lengthText":{"accessibility":{"accessibilityData":{"label":"', '"}}', False),
             'descrição_do_vídeo': parser.parser(html_baixado, '"shortDescription":"', '","isCrawlable"', False),
             'data_de_publicação': parser.parser(html_baixado, '"Published on ', '"},', False),
             'url_do_canal': parser.parser(html_baixado, '{"browseId":"', '"}}}]},', False),
             'query': parser.parser(html_baixado, '"searchEndpoint":{"query":"', '"}}', False),
             'recomendados_pelo_youtube': parser.list_datas(html_baixado,
                                                            '"title":{"accessibility":{"accessibilityData":{"label":"',
                                                            '"}},"simpleText":"')
             }
    return dados
