from getMotivation import get_motivation_quote
from getNews import get_business_news
from getPrices import get_market_prices, get_gold_price
from sendMsg import send_telegram_message


def main():
  # Fetching data
  quote, author = get_motivation_quote()
  gold_price = get_gold_price()
  nifty_price, sensex_price = get_market_prices()
  news_title, news_description, news_url = get_business_news()

  # Constructing the message
  msg_body = (
      f"Quote: {quote}\n-{author}\n\n\n"
      f"Markets ===================\n\n"
      f"Nifty Price: {nifty_price}\nSensex Price: {sensex_price}\nGold Price: {gold_price}\n\n"
      f"Markets ===================\n\n"
      f"Business News:\n{news_title}\n{news_url}")

  # Sending the message
  response_code = send_telegram_message(msg_body)
  print(f"Response Code: {response_code}")


if __name__ == "__main__":
  main()
