import yfinance as yf


def get_market_prices():
    try:
        nifty = yf.Ticker("^NSEI")
        sensex = yf.Ticker("^BSESN")

        nifty_data = nifty.history(period="5d")
        sensex_data = sensex.history(period="5d")

        if nifty_data.empty:
            raise ValueError("No data returned for Nifty")
        if sensex_data.empty:
            raise ValueError("No data returned for Sensex")

        nifty_price = nifty_data['Close'].iloc[-1]
        sensex_price = sensex_data['Close'].iloc[-1]

        return nifty_price, sensex_price

    except Exception as e:
        print(f"Error fetching market prices: {e}")
        return None, None  # Return None values in case of an error


def get_gold_price():
    try:
        gold = yf.Ticker("GC=F")
        gold_data = gold.history(period="5d")

        if gold_data.empty:
            raise ValueError("No data returned for Gold")

        gold_price = gold_data['Close'].iloc[-1]
        return round(gold_price, 2)

    except Exception as e:
        print(f"Error fetching gold price: {e}")
        return None  # Return None in case of an error
