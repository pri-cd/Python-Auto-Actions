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


# Function to get a motivational quote
def getMotivation():
  """
  response = requests.get('https://zenquotes.io/api/random')
  data = response.json()
  quot = data[0]['q'] + " -" + data[0]['a']
  print(quot)
  return quot
  """
  professional_quotes = [
      "The only way to do great work is to love what you do. -Steve Jobs",
      "Success is not the key to happiness. Happiness is the key to success. -Albert Schweitzer",
      "The way to get started is to quit talking and begin doing. -Walt Disney",
      "Success usually comes to those who are too busy to be looking for it. -Henry David Thoreau",
      "Don’t be afraid to give up the good to go for the great. -John D. Rockefeller",
      "If you really look closely, most overnight successes took a long time. -Steve Jobs",
      "Opportunities don't happen. You create them. -Chris Grosser",
      "Success is not in what you have, but who you are. -Bo Bennett",
      "I find that the harder I work, the more luck I seem to have. -Thomas Jefferson",
      "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
      "Hard work beats talent when talent doesn’t work hard. -Tim Notke",
      "Don’t watch the clock; do what it does. Keep going. -Sam Levenson",
      "The future depends on what you do today. -Mahatma Gandhi",
      "The way to achieve your own success is to be willing to help somebody else get it first. -Iyanla Vanzant",
      "Success is not final; failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
      "Success is walking from failure to failure with no loss of enthusiasm. -Winston Churchill",
      "The only place where success comes before work is in the dictionary. -Vidal Sassoon",
      "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. -Roy T. Bennett",
      "Believe you can and you’re halfway there. -Theodore Roosevelt",
      "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. -Steve Jobs",
      "Success is the sum of small efforts, repeated day in and day out. -Robert Collier",
      "You miss 100% of the shots you don’t take. -Wayne Gretzky",
      "Success is not measured by what you accomplish, but by the opposition you have encountered, and the courage with which you have maintained the struggle against overwhelming odds. -Orison Swett Marden",
      "Do not be embarrassed by your failures, learn from them and start again. -Richard Branson",
      "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
      "It is never too late to be what you might have been. -George Eliot",
      "What you get by achieving your goals is not as important as what you become by achieving your goals. -Zig Ziglar",
      "Success is liking yourself, liking what you do, and liking how you do it. -Maya Angelou",
      "If you don’t design your own life plan, chances are you’ll fall into someone else’s plan. -Jim Rohn",
      "Success is a journey, not a destination. The doing is often more important than the outcome. -Arthur Ashe",
      "Act as if what you do makes a difference. It does. -William James",
      "The successful warrior is the average man, with laser-like focus. -Bruce Lee",
      "Don’t count the days, make the days count. -Muhammad Ali",
      "Your time is limited, don’t waste it living someone else’s life. -Steve Jobs",
      "You don’t have to be great to start, but you have to start to be great. -Zig Ziglar",
      "Success is getting what you want, happiness is wanting what you get. -W. P. Kinsella",
      "It does not matter how slowly you go, as long as you do not stop. -Confucius",
      "Success is not how high you have climbed, but how you make a positive difference to the world. -Roy T. Bennett",
      "The best way to predict the future is to create it. -Peter Drucker",
      "Do not wait to strike till the iron is hot; but make it hot by striking. -William Butler Yeats",
      "The only way to achieve the impossible is to believe it is possible. -Charles Kingsleigh",
      "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
      "The difference between who you are and who you want to be is what you do. -Unknown",
      "The secret of success is to do the common thing uncommonly well. -John D. Rockefeller Jr."
  ]

  quote = random.choice(professional_quotes)
  print(quote)
  return quote


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
  motivation = getMotivation()
  gold, nifty, sensex = getPrices()
  title, description, url = getNews()

  msgBody = f"Quote: {motivation}\n\n\n" + "Markets ===================\n\n" + f"Nifty Price: {nifty}\nSensex Price: {sensex}\nGold Price: {gold}\n\n" + "Markets ===================\n\n" + f"Business News:\n{title}\n{url}"
  # Send The Msg
  print(f"Response Code: {sendMessage(body=msgBody)}")


if __name__ == "__main__":
  main()
