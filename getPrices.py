import yfinance as yf


def get_market_prices():
    nifty = yf.Ticker("^NSEI")
    sensex = yf.Ticker("^BSESN")

    nifty_price = nifty.history(period="1d")['Close'].iloc[-1]
    sensex_price = sensex.history(period="1d")['Close'].iloc[-1]

    return nifty_price, sensex_price


def get_gold_price():
    gold = yf.Ticker("GC=F")
    gold_price = gold.history(period="1d")['Close'].iloc[-1]

    return round(gold_price, 2)
