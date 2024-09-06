from time import sleep
from datetime import datetime, timezone, timedelta
import requests
import os

gNewsUrl = "https://gnews.io/api/v4/top-headlines"


def getTime():
    now_utc = datetime.now(timezone.utc)
    formatted_time = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    print("Formatted UTC Time:", formatted_time)
    return formatted_time


def get_business_news():
    apiKey = os.getenv('NEWS_API_KEY')
    params = {
        'category': 'business',
        'lang': 'en',
        'country': 'in',
        'max': 1,
        'apikey': apiKey
    }

    try:
        resp = requests.request(method='GET', url=gNewsUrl, params=params)
    except Exception as exe:
        print(
            f"Exception Occured While Fetching News Using- GNEWS API!- {exe}")
        return None, None, None

    articles = resp.json().get('articles', [])
    title, desc, url = None, None, None

    for article in articles:
        title = article.get('title', 'No Title')
        desc = article.get('description', 'No Description')
        url = article.get('url', 'No URL')

    print(title, desc, url, sep="\n")
    return title, desc, url
