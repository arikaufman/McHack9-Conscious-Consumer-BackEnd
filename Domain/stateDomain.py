from Domain.state import State
from Domain.companyDomain import companyDomain
from Common.webscraper import  webScraper

class stateDomain:
   def get(state):
      #Workaround for dynamic scraping challenges,
      #would automatically plug state name into webscraper so no data would have to be hard coded
      url = ""
      if state.name == "Walmart":
         url = "https://www.sustainalytics.com/esg-rating/walmart-inc/1008191301"
      if state.name == "Amazon":
         url = "https://www.sustainalytics.com/esg-rating/amazon-com-inc/1007896995"
      if state.name == "Starbucks":
         url = "https://www.sustainalytics.com/esg-rating/starbucks-corp/1007912991"
      state.esgRating = webScraper.extractesgscore(url)
      return state