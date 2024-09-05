import requests
import os


def get_business_news():
    api_key = os.getenv('NEWS_API_KEY')
    print(f"NEWS API-KEY: {api_key}")
    url = 'https://newsapi.org/v2/top-headlines'

    params = {'category': 'business', 'country': 'in', 'apiKey': api_key}

    response = requests.get(url, params=params)
    news = response.json()
    print(news)

    if news['status'] == 'ok' and news['totalResults'] > 0:
        article = news['articles'][0]
        return article['title'], article['description'], article['url']
    else:
        return "No Title", "No Description", "No URL"
