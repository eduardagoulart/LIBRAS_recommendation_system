import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import proccess_data
import csv


'''
    Bot para abrir o navegador e buscar um conteúdo
'''


def search_element():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/?feature=youtu.be")
    assert "YouTube" in driver.title
    elem = driver.find_element_by_name("search_query")
    elem.clear()
    elem.send_keys("turma da monica libras")
    elem.send_keys(Keys.RETURN)
    # video = driver.find_element_by_id('video-title').click()
    assert "No results found." not in driver.page_source


''' 
    Function will charge the whole page
'''


def scroll_down(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
    except:
        driver.refresh()
        driver.get(url)
    html = driver.page_source
    if proccess_data.return_informations(html):
        return html
    else:
        last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height
        flag_click = 0  # flag_click evita que clique em lugar que não existe
        while True:
            # Scroll down to bottom
            if len([(a.end()) for a in list(re.finditer("não contribuiu ainda.", html))]) > 0:
                lista = []
                return lista
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if flag_click == 0:  # é só na primeira parte que esse botão aparece
                try:
                    driver.find_element_by_class_name(
                        'social-common-ShowMore__button_text--3mpZC').click()  # aqui vai permitir eu clicar na página para descer
                except:  # quer dizer que não precisa clicar em nada
                    pass
                flag_click = 1

            # Wait to load page
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                html = driver.page_source
                break
            last_height = new_height
            return html


if '__main__' == __name__:
    """
    links = ['https://www.youtube.com/watch?v=WDHFOT_XNRE', 'https://www.youtube.com/watch?v=vHitwM1SROk', 
            'https://www.youtube.com/watch?v=Ueb_qIEs3q0', 'https://www.youtube.com/watch?v=YmPKpoqUiCM',
            ]
    data = []
    for i in links:
        html = scroll_down(i)
        data.append(proccess_data.return_informations(html))

    with open('video.csv', mode='w') as csv_file:
        fieldnames = ['nome_do_vídeo', 'autor', 'likes', 'deslikes', 'visualização', 'descrição_do_vídeo',
                      'data_de_publicação', 'url_do_canal', 'query', 'recomendados_pelo_youtube']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in data:
            writer.writerow(i)
    """
    html = scroll_down('https://www.youtube.com/watch?v=IWs8b1ekVsQ')
    # html = scroll_down("https://www.youtube.com/watch?v=Ueb_qIEs3q0")

    data = proccess_data.return_informations(html)

    with open('video.csv', mode='w') as csv_file:
        fieldnames = ['nome_do_vídeo', 'autor', 'likes', 'deslikes', 'visualização', 'descrição_do_vídeo',
                      'data_de_publicação', 'url_do_canal', 'query', 'recomendados_pelo_youtube']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

