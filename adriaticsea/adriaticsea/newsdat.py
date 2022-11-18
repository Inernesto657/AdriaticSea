from pytrends.request import TrendReq
from GoogleNews import GoogleNews
import pandas as pd

# Input of country has to go in countries array
countries=["canada"]
pytrends = TrendReq(hl='en-US',tz=360)

class newsdat():          
    def __init__(self):   
        self.country = None  
        self.trend = None
        self.title = None
        self.image = None
        self.posted = None
        self.posteddatetime = None
        self.detailednews = None 
        self.description = None

    def trendingSearches(countries):
      filteredNews = []
      for country in countries:
        try:
          data = pytrends.trending_searches (country)
          for i in range(len(data)):
            news = GoogleNews(period='1d')
            news.search(str(data.loc[i, 0]))
            result = news.result()
            for res in result:
              oNew = newsdat()
              oNew.country = country
              oNew.trend = str(data.loc[i, 0])
              oNew.title = str(res["title"])
              oNew.image = str(res["img"])
              oNew.posted = str(res["date"])
              oNew.posteddatetime = str(res["datetime"])
              oNew.detailednews = str(res["link"])
              oNew.description = str(res["desc"])
              filteredNews.append(oNew)
        except:
          data = []

      return filteredNews