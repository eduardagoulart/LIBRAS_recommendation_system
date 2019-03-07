from bs4 import BeautifulSoup
import re


def parser_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    info = {'title': title}
    hyper_link = soup.find_all('div')
    div = BeautifulSoup(html, 'html.parser')
    for i in range(len(hyper_link)):
        t = div.string
        # print(t)
    # print(hyper_link)
    info['hyper_link'] = hyper_link
    # a = soup.get_text()
    return title


def parser(html):
    clean = re.compile('<.*?>')
    clean_test = re.sub(clean, '', html)
    x = re.search("likes$", clean_test)
    print(x)
    return clean_test
