import json
import parser


def return_informations(html_baixado):

    numero_likes = parser.parser(html_baixado, 'tooltip":"', "\"}}", True)
    numero_likes = numero_likes.split(' / ')

    dados = {'nome do vídeo': parser.parser(html_baixado, 'title":"', '","', False),
             'autor': parser.parser(html_baixado, '","author":"', '",', False),
             'likes': numero_likes[0],
             'deslikes': numero_likes[1],
             'visualização': parser.parser(html_baixado, 'viewCount":"', '",', True),
             'descrição do vídeo': parser.parser(html_baixado, '"shortDescription":"', '","isCrawlable"', False),
             'data de publicação': parser.parser(html_baixado, '"Published on ', '"},', False),
             'url do canal': parser.parser(html_baixado, '{"browseId":"', '"}}}]},', False),
             'query': parser.parser(html_baixado, '"searchEndpoint":{"query":"', '"}}', False),
             'recomendados pelo youtube': parser.list_datas(html_baixado, '"title":{"accessibility":{"accessibilityData":{"label":"', '"}},"simpleText":"')
             }

    with open('data.json', 'w', encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False)
