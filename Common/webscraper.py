import requests
#from html.parser import HTMLParser
#from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

class webScraper:
    def extractesgscore(url):
        URL_company = url
        html_company = requests.get(URL_company)

        soup = BeautifulSoup(html_company.content, "html.parser")
        rating = soup.find('div', {"class" : "col-6 risk-rating-score"})
        return rating.text