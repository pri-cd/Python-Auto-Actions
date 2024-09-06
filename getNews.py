from time import sleep
import requests
import os
from requests_html import HTMLSession

gUrl = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"


def get_business_news():
    session = HTMLSession()
    r = session.get(gUrl)
    r.html.render(sleep=1, scrolldown=5)

    #find all the articles by using inspect element and create blank list
    articles = r.html.find('article')
    newslist = []

    for article in articles:
        try:
            newsItem = article.find('h3', first=True)
            title = newsItem.text
            link = newsItem.absoulte_links

            newslist.append({'Title': title, "Link": link})
        except:
            pass

    print(newslist)


if __name__ == "__main__":
    get_business_news()
