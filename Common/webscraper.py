import requests
from html.parser import HTMLParser
#from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

URL = "https://www.sustainalytics.com/esg-ratings/amazon-com-inc/1007896995"
page = requests.get(URL)
print(page.text)

class FindRating(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.countLanguages = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'col-6 risk-rating-score':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'div' and self.inLink and data.strip():
            print(data)

parser = FindRating()
parser.feed(page.text)