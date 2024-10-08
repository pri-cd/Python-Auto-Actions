from getMotivation import get_motivation_quote
from getNews import get_business_news
from getPrices import get_market_prices, get_gold_price
from sendMsg import send_telegram_message


def prepareBody(quote, author, nifty, sensex, gold, news, newsUrl):
  # Constructing the message
  msg_body = [
      f"Quote:\n\"{quote}\"\n-{author}",
      f"Nifty Price: {nifty}\nSensex Price: {sensex}\nGold Price: {gold}",
      f"Business News:\n{news}\n\n{newsUrl}"
  ]
  print(msg_body)
  return msg_body


def main():
  # Fetching data
  quote, author = get_motivation_quote()
  gold_price = get_gold_price()
  nifty_price, sensex_price = get_market_prices()
  news_title, news_description, news_url = get_business_news()

  body = prepareBody(quote=quote,
                     author=author,
                     nifty=nifty_price,
                     sensex=sensex_price,
                     gold=gold_price,
                     news=news_title,
                     newsUrl=news_url)

  # Sending the message
  response_code = send_telegram_message(body)
  print(f"Response Code: {response_code}")


if __name__ == "__main__":
  main()
