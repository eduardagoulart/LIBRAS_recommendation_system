import re
from selenium import webdriver


def baixa_le_navegador(url, driver):
    try:
        driver.get(url)
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    except:
        driver.refresh()  # é pq não consegui carregar a página sozinha
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    return html


def parser(html, token_pesquisa, token_parada, regex_numeral):
    intervalo_inicio = [(a.end()) for a in list(re.finditer(token_pesquisa, html))]
    p_break = [(a.start()) for a in list(re.finditer(token_parada, html))]

    i = 0
    if regex_numeral:
        while i < len(intervalo_inicio):
            if not re.match("[0-9]", html[intervalo_inicio[i]].lower()):
                intervalo_inicio.pop(i)
                i -= 1
            i += 1

    if len(intervalo_inicio) == 0 or len(p_break) == 0:
        return None
    else:
        intervalo_inicio = intervalo_inicio[0]
        for i in p_break:
            if i > intervalo_inicio:  # no primeiro ponto que a posição de pBreak for maior que p eu assumo aquele valor como valor de break do while que vai estar lá em baixo
                p_break = i
                break
    info = ''
    while intervalo_inicio < p_break:
        info += html[intervalo_inicio]
        intervalo_inicio += 1

    return info


def string_and_data(html, token_pesquisa, token_parada):
    intervalo_inicio = [(a.end()) for a in list(re.finditer(token_pesquisa, html))]
    p_break = [(a.start()) for a in list(re.finditer(token_parada, html))]

    inicio = []
    fim = []
    print(p_break[0])
    print(intervalo_inicio[0])
    for a in range(len(list(re.finditer(token_pesquisa, html)))):
        if p_break[a] < intervalo_inicio[a]:
            inicio.append(intervalo_inicio[a])
            fim.append(p_break[a])
        else:
            while p_break[a] > intervalo_inicio[a]:
                a += 1
                p_break[a] = intervalo_inicio[a]

    lista_info = []
    for i in range(len(inicio)):
        info = ''
        while inicio[i] < fim[i]:
            info += html[intervalo_inicio[i]]
            fim[i] += 1
            if inicio[i] <= fim[i]:
                lista_info.append(info)
                break
            # print(info)
    print(lista_info)


    '''
    intervalo_inicio = intervalo_inicio[0]
    for i in p_break:
        if i > intervalo_inicio:  # no primeiro ponto que a posição de pBreak for maior que p eu assumo aquele valor como valor de break do while que vai estar lá em baixo
            p_break = i
            break
    info = ''
    while intervalo_inicio < p_break:
        info = info + html[intervalo_inicio]
        intervalo_inicio = intervalo_inicio + 1

    # return info'''


def return_informations():
    driver = webdriver.Chrome()
    html_baixado = baixa_le_navegador('https://www.youtube.com/watch?v=WDHFOT_XNRE', driver)

    f = open('index.html', 'w')
    f.write(html_baixado)

    numero_likes = parser(html_baixado, 'tooltip":"', "\"}}", True)
    numero_likes = numero_likes.split(' / ')
    print("Número de Likes ", numero_likes[0])
    print("Número de Dislikes ", numero_likes[1])
    author = parser(html_baixado, '","author":"', '",', False)
    print(f'Autor: {author}')
    view = parser(html_baixado, 'viewCount":"', '",', True)
    print(f'Visualizações: {view}')
    month_published = parser(html_baixado, '"Published on ', ' ', False)
    print(f'Data da publicação: {month_published}')
    aux = '"Published on ' + month_published
    print(aux)
    day_published = parser(html_baixado, aux, ',', True)
    print(f"Day and year {day_published}")
    nome_video = parser(html_baixado, 'title":"', '",', False)
    print("Nome do Vídeo ", nome_video)

    description = parser(html_baixado, '"shortDescription":"', '","isCrawlable"', False)
    print(f"Descrição do vídeo: {description}")

    browser_id = parser(html_baixado, '{"browseId":"', '"}}}]},', False)
    print(f'URL do canal {browser_id}')
    published = parser(html_baixado, '"Published on ', '"},', False)
    print(f'Data da publicação: {published}')

    query = parser(html_baixado, '"searchEndpoint":{"query":"', '"}}', False)
    print(f'Query: {query}')

    continue_assistindo = string_and_data(html_baixado, '"title":{"accessibility":{"accessibilityData":{"label":"',
                                          '"}},"simpleText":"')
    # print(f'Continue assistindo: {continue_assistindo}')

    driver.close()


if __name__ == '__main__':
    return_informations()
