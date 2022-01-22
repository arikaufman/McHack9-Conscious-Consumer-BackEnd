import requests
#from html.parser import HTMLParser
#from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

URL_homepage = "https://www.sustainalytics.com/esg-ratings"
html_home = requests.get(URL_homepage)
URL_company = "https://www.sustainalytics.com/esg-rating/cisco-systems-inc/1007897937"
html_company = requests.get(URL_company)

print(html_company.text)

soup = BeautifulSoup(html_company.content, "html.parser")
rating = soup.find('div', {"class" : "col-6 risk-rating-score"})
print(rating.text)

