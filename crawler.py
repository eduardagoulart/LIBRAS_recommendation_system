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

    links = ['https://www.youtube.com/watch?v=WDHFOT_XNRE', 'https://www.youtube.com/watch?v=vHitwM1SROk',
             'https://www.youtube.com/watch?v=Ueb_qIEs3q0', 'https://www.youtube.com/watch?v=YmPKpoqUiCM',
             'https://www.youtube.com/watch?v=IWs8b1ekVsQ', 'https://www.youtube.com/watch?v=Re9ASuOXiwM',
             'https://www.youtube.com/watch?v=zEZtQZtw2xA', 'https://www.youtube.com/watch?v=hL1WCuEoCG0',
             'https://www.youtube.com/watch?v=2fdCB_JlQjw', 'https://www.youtube.com/watch?v=TFVTYaXV314',
             'https://www.youtube.com/watch?v=8Jw8QcTRWuc', 'https://www.youtube.com/watch?v=YBtWdx4xObs',
             'https://www.youtube.com/watch?v=YBtWdx4xObs', 'https://www.youtube.com/watch?v=1J7QdEzSyhs',
             'https://www.youtube.com/watch?v=PugIcPzwoD8', 'https://www.youtube.com/watch?v=FSx0zF7Z6XQ',
             'https://www.youtube.com/watch?v=Y3m1ye7RJ0A', 'https://www.youtube.com/watch?v=thCm4vnM2LA',
             'https://www.youtube.com/watch?v=zz4rmjL2nFA&t=2s', 'https://www.youtube.com/watch?v=Ha5eP8p_JKg',
             'https://www.youtube.com/watch?v=kIXKrh00Og8', 'https://www.youtube.com/watch?v=fxVIPKuMe6k',
             'https://www.youtube.com/watch?v=RAtvfTC2AbU', 'https://www.youtube.com/watch?v=fdyuWRRjIEQ',
             'https://www.youtube.com/watch?v=7jsJW10LJGA', 'https://www.youtube.com/watch?v=BMIHzgDDKrc',
             'https://www.youtube.com/watch?v=u4QJygwAdW0', 'https://www.youtube.com/watch?v=qfXDjWHnmcc',
             'https://www.youtube.com/watch?v=5lPdTuhast0', 'https://www.youtube.com/watch?v=4VynqNTsG7A',
             'https://www.youtube.com/watch?v=yipGWYQQsS8', 'https://www.youtube.com/watch?v=MnxYr6vj1WQ&t=18s',
             'https://www.youtube.com/watch?v=pK4rIVOySKE', 'https://www.youtube.com/watch?v=nI9IMQOTzag',
             'https://www.youtube.com/watch?v=kuJFNEoFBSI', 'https://www.youtube.com/watch?v=JKqnrBaGbs8',
             'https://www.youtube.com/watch?v=hnln_GU-M98', 'https://www.youtube.com/watch?v=zhpo0NgjpcM',
             'https://www.youtube.com/watch?v=IAG43Witg3I', 'https://www.youtube.com/watch?v=ZaFgk5ekhC4',
             'https://www.youtube.com/watch?v=1J7QdEzSyhs&t=1s', 'https://www.youtube.com/watch?v=UeEuLkNxlMQ',
             'https://www.youtube.com/watch?v=3JGCKzPDe4Q', 'https://www.youtube.com/watch?v=DxuHClptKoE',
             'https://www.youtube.com/watch?v=rgCpu3BcxmM', 'https://www.youtube.com/watch?v=GcowO23lzMk',
             'https://www.youtube.com/watch?v=a3FZLqwucIM', 'https://www.youtube.com/watch?v=8LnwkL80HbE',
             'https://www.youtube.com/watch?v=hYqNrrF5z6g', 'https://www.youtube.com/watch?v=6llgCt4OMRA',
             'https://www.youtube.com/watch?v=zNCczm3jzgo', 'https://www.youtube.com/watch?v=OzbwZtT4KDo',
             'https://www.youtube.com/watch?v=dJed8tRy0SY', 'https://www.youtube.com/watch?v=BHYuCIuvjnE',
             'https://www.youtube.com/watch?v=81q4IlKHJhc', 'https://www.youtube.com/watch?v=ILQgw6siK14',
             'https://www.youtube.com/watch?v=4v8NkVqzafg', 'https://www.youtube.com/watch?v=Kx3JV2UuXFE',
             'https://www.youtube.com/watch?v=JuCVU9rGUa8', 'https://www.youtube.com/watch?v=7q1kF5N1gHs&t=85s',
             'https://www.youtube.com/watch?v=feBeOzpw2Xc', 'https://www.youtube.com/watch?v=mgSIYg-Astg',
             'https://www.youtube.com/watch?v=ouDNMKuQkiY', 'https://www.youtube.com/watch?v=LFCr4QNW-x8',
             'https://www.youtube.com/watch?v=rSKlm0S_5YQ', 'https://www.youtube.com/watch?v=eXbN6RYH6gk',
             'https://www.youtube.com/watch?v=Z0JvlMRNzek', 'https://www.youtube.com/watch?v=1BahR0kmtCA',
             'https://www.youtube.com/watch?v=xmfQz21LPkY', 'https://www.youtube.com/watch?v=LOJlL6P9LQ0',
             'https://www.youtube.com/watch?v=fVPGLJy4zP0&t=2349s', 'https://www.youtube.com/watch?v=UBwGCy14JMk',
             'https://www.youtube.com/watch?v=KmiQ82ynDkg', 'https://www.youtube.com/watch?v=wKqqaaDnaBI',
             'https://www.youtube.com/watch?v=SJWDICzqyPQ', 'https://www.youtube.com/watch?v=ndqVp-pr6T0',
             'https://www.youtube.com/watch?v=snNKbuFlro0', 'https://www.youtube.com/watch?v=hCY8gLYyEI8',
             'https://www.youtube.com/watch?v=nXI4aO2_G3E', 'https://www.youtube.com/watch?v=RzS5_aSxK0U',
             'https://www.youtube.com/watch?v=lg2JWcaxy-s', 'https://www.youtube.com/watch?v=X_GGQelOsUk',
             'https://www.youtube.com/watch?v=yG3ntH2d0XQ', 'https://www.youtube.com/watch?v=fsKJkOzdZYk',
             'https://www.youtube.com/watch?v=8uOp2wapJ4w', 'https://www.youtube.com/watch?v=CiCEORn-1yM',
             'https://www.youtube.com/watch?v=Z0JvlMRNzek&t=24s', 'https://www.youtube.com/watch?v=DmMdfpXXjz8',
             'https://www.youtube.com/watch?v=uEU8p9Gw7TY', 'https://www.youtube.com/watch?v=xtEeh8F1HE0',
             'https://www.youtube.com/watch?v=jEN4lftLxd4', 'https://www.youtube.com/watch?v=WH9A-mzcq7U',
             'https://www.youtube.com/watch?v=fq034k55-kA', 'https://www.youtube.com/watch?v=z67NvKCsQE0',
             'https://www.youtube.com/watch?v=AbY6AmJwA40', 'https://www.youtube.com/watch?v=fremAl8802s',
             'https://www.youtube.com/watch?v=KmIYadjJO8U', 'https://www.youtube.com/watch?v=16qND1yhi9E',
             'https://www.youtube.com/watch?v=bhagSKWAYBc', 'https://www.youtube.com/watch?v=neIJQzyr_xc',
             'https://www.youtube.com/watch?v=tl5pRAtlOsY', 'https://www.youtube.com/watch?v=DmMdfpXXjz8&t=6s',
             'https://www.youtube.com/watch?v=feNEaOQRAOc', 'https://www.youtube.com/watch?v=xQyAPxv1QWI',
             'https://www.youtube.com/watch?v=xD9klMZs3aw', 'https://www.youtube.com/watch?v=fsKJkOzdZYk&t=2s',
             'https://www.youtube.com/watch?v=eXbN6RYH6gk&t=46s', 'https://www.youtube.com/watch?v=J_Q75DiciJY',
             'https://www.youtube.com/watch?v=LFCr4QNW-x8&t=31s', 'https://www.youtube.com/watch?v=QhWSohfQhC8',
             'https://www.youtube.com/watch?v=tGS9tMzC10Q', 'https://www.youtube.com/watch?v=xuwC4UEf65c',
             'https://www.youtube.com/watch?v=4ziBIATB5gs', 'https://www.youtube.com/watch?v=lg2JWcaxy-s&t=1s',
             'https://www.youtube.com/watch?v=bdQudfWfLg4', 'https://www.youtube.com/watch?v=0tzFlKg1e4I',
             'https://www.youtube.com/watch?v=JI4gtl757a0', 'https://www.youtube.com/watch?v=HlEZsDdjNoQ',
             'https://www.youtube.com/watch?v=xfzE49pWHVU', 'https://www.youtube.com/watch?v=S8GL5sjjD7w',
             'https://www.youtube.com/watch?v=8_GHftBajtU']
    data = []
    for i in links:
        html = scroll_down(i)
        data.append(proccess_data.return_informations(html))

    with open('video.csv', mode='w') as csv_file:
        fieldnames = ['nome_do_vídeo', 'autor', 'likes', 'deslikes', 'visualização', 'duração_do_video',
                      'descrição_do_vídeo', 'data_de_publicação', 'url_do_canal', 'query', 'recomendados_pelo_youtube']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in data:
            writer.writerow(i)
    """
    html = scroll_down('https://www.youtube.com/watch?v=S8GL5sjjD7w')
    # html = scroll_down("https://www.youtube.com/watch?v=Ueb_qIEs3q0")

    data = proccess_data.return_informations(html)

    with open('video.csv', mode='w') as csv_file:
        fieldnames = ['nome_do_vídeo', 'autor', 'likes', 'deslikes', 'visualização', 'duração_do_video',
                      'descrição_do_vídeo', 'data_de_publicação', 'url_do_canal', 'query', 'recomendados_pelo_youtube']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
    """
