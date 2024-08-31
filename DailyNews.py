'''
@Task At Hand: 
Send me using my Mail a Message Daily That Conatains!:
1. Motivational Quotes
2. Nifty & Sensex Price
3. Gold Prices. 
4. One Important Business News.


@Solution: 
1. Use "yFinance" API for the Prices
2. For Motivational Quote: Use "zenquotes" API
3. For News use "newsapi" API
'''

import requests
import os
import yfinance as yf
import random


# Get Quote!
def getMotivationAPI(url=baseUrl, path='/quotes/random'):
  completeUrl = f"{url}{path}"
  print(completeUrl)
  payload = {}
  headers = {}

  params = {
      "maxLength": 300,
      "minLength": 100,
      "tags": "Sucess|Technology|Wisdom",
      "author": "",
      "query": 1,
      "limit": 5
  }
  quotes = requests.request(method="GET",
                            url=completeUrl,
                            headers=headers,
                            params=params,
                            data=payload).json()

  rdQuotes = random.choice(quotes)
  quote = rdQuotes['content']
  author = rdQuotes['author']
  return quote, author


# Function To Get News
def getNews():
  apiKey = os.getenv('NEWS_API_KEY')
  print(apiKey, '<---------------------')
  url = 'https://newsapi.org/v2/top-headlines'
  params = {
      'category': 'business',
      'country': 'in',  # You can change this to your desired country
      'apiKey': apiKey  # Replace with your NewsAPI key
  }

  response = requests.get(url, params=params)
  news = response.json()
  if news['status'] == 'ok' and news['totalResults'] > 0:
    article = news['articles'][0]
    title = article['title']
    description = article['description']
    url = article['url']  # Get the URL of the news article
    print(title, description, url, sep=' | ')
    return title, description, url
  else:
    return "No news found", "There is no business news available at the moment.", "None"


# Functions To Get The Nifty, Sensex, Gold Prices!-
def getMarketPrices():
  nifty = yf.Ticker("^NSEI")
  sensex = yf.Ticker("^BSESN")
  nifty_price = nifty.history(period="1d")['Close'].iloc[-1]
  sensex_price = sensex.history(period="1d")['Close'].iloc[-1]
  return nifty_price, sensex_price


def getGoldPrices():
  gold = yf.Ticker("GC=F")
  gold_price = gold.history(period="1d")['Close'].iloc[-1]
  return round(gold_price, 2)


def getPrices():
  print(getGoldPrices(), *getMarketPrices(), sep=" | ")
  return getGoldPrices(), *getMarketPrices()


def sendMessage(body):
  bot_token = os.getenv('TG_CHAT_TOKEN')
  chat_id = os.getenv('TG_CHAT_ID')
  print(bot_token, '<---------------------')
  print(chat_id, '<---------------------')

  url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
  payload = {'chat_id': chat_id, 'text': body}
  response = requests.post(url, data=payload)
  return response.status_code


def main():
  quote, auth = getMotivationAPI()
  gold, nifty, sensex = getPrices()
  title, description, url = getNews()

  msgBody = f"Quote: {quote}\n-{auth}\n\n\n" + "Markets ===================\n\n" + f"Nifty Price: {nifty}\nSensex Price: {sensex}\nGold Price: {gold}\n\n" + "Markets ===================\n\n" + f"Business News:\n{title}\n{url}"
  # Send The Msg
  print(f"Response Code: {sendMessage(body=msgBody)}")


if __name__ == "__main__":
  main()
