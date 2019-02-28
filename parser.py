from html.parser import HTMLParser
from crawler import scroll_down
import json


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print("Encountered some data  :", data)
        # print(type(data))


parser = MyHTMLParser()
parser.feed(scroll_down('https://www.youtube.com/watch?v=WDHFOT_XNRE'))

# json_data = json.dumps(str(data))
