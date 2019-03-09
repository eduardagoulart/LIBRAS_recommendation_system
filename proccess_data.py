import json
import parser


def return_informations(html_baixado):

    numero_likes = parser.parser(html_baixado, 'tooltip":"', "\"}}", True)
    numero_likes = numero_likes.split(' / ')
    print("Número de Likes ", numero_likes[0])
    print("Número de Dislikes ", numero_likes[1])
    author = parser.parser(html_baixado, '","author":"', '",', False)
    print(f'Autor: {author}')
    view = parser.parser(html_baixado, 'viewCount":"', '",', True)
    print(f'Visualizações: {view}')

    nome_video = parser.parser(html_baixado, 'title":"', '","', False)
    print("Nome do Vídeo ", nome_video)

    description = parser.parser(html_baixado, '"shortDescription":"', '","isCrawlable"', False)
    print(f"Descrição do vídeo: {description}")

    browser_id = parser.parser(html_baixado, '{"browseId":"', '"}}}]},', False)
    print(f'URL do canal {browser_id}')
    published = parser.parser(html_baixado, '"Published on ', '"},', False)
    print(f'Data da publicação: {published}')

    query = parser.parser(html_baixado, '"searchEndpoint":{"query":"', '"}}', False)
    print(f'Query: {query}')

    s = parser.list_datas(html_baixado, '"title":{"accessibility":{"accessibilityData":{"label":"', '"}},"simpleText":"')
    dados = {'nome do vídeo': nome_video,
             'autor': author,
             'likes': numero_likes[0],
             'deslikes': numero_likes[1],
             'visualização': view,
             'descrição do vídeo': description,
             'data de publicação': published,
             'url do canal': browser_id,
             'query': query,
             'recomendados pelo youtube': s
             }

    with open('data.json', 'w', encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False)
