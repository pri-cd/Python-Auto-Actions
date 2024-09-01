# Daily Automation 🕰️

Welcome to **Daily Automation**—your personal assistant for staying motivated, updated, and informed every day! This project is a delightful blend of technology and daily routines, fetching motivational quotes, stock market prices, gold prices, and the latest business news, and delivering them directly to your Telegram.

![Daily Automation](https://github.com/pri-cd/Python-Auto-Actions/blob/main/Automation.jpg)  
*Stay motivated and informed, every day.*

## 🌟 Features

- **✨ Daily Motivation**: Start your day with an inspiring quote.
- **📈 Market Insights**: Keep track of the latest Nifty, Sensex, and Gold prices.
- **📰 Business Updates**: Get the top business news headlines.
- **🚀 Telegram Integration**: Receive all the updates directly in your Telegram chat.

## 🗂️ Project Structure

- **`DailyNews.py`**: The central script that orchestrates data collection and message delivery.
- **`getMotivation.py`**: Fetches a random motivational quote.
- **`getNews.py`**: Retrieves the latest business news.
- **`getPrices.py`**: Gets Nifty, Sensex, and Gold prices.
- **`sendMsg.py`**: Handles sending messages to your Telegram bot subscribers.
- **`requirements.txt`**: Lists all necessary Python packages.
- **`.github/workflows/main.yml`**: Automates daily script execution via GitHub Actions.

## 🛠️ Setup

### Prerequisites

- Python 3.x
- A Telegram bot and API token
- NewsAPI key
- GitHub account for GitHub Actions setup

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/daily-automation.git
   cd daily-automation

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Configure environment variables:**
- **`NEWS_API_KEY`**: Your NewsAPI key.
- **`TG_CHAT_TOKEN`**: Your Telegram bot API token.


### Running Locally:
   ```bash
   python DailyNews.py
   ```

## 📁 Message Format
   ```yaml
   Quote: [Inspirational Quote]
   - [Author]
   
   Markets ===================
   
   Nifty Price: [Nifty Price]
   Sensex Price: [Sensex Price]
   Gold Price: [Gold Price]
   
   Markets ===================
   
   Business News:
   [News Title]
   [News URL]
   ```

## 📁 Contribution: 
- This is a personal project, but suggestions and contributions are always **welcome**!
- Feel free to fork the repo, make changes, and submit a pull request.

## 🙌 Acknowledgments:

- **Quotable API**: For daily motivation.
- **NewsAPI**: For the latest business news. (* Requires API key *)
- **Yahoo Finance**: For stock and gold prices.
- **Telegram API**: For message delivery.


## Note: 
- Thank you for checking out Daily Automation! I hope it makes your day a little brighter and more informed. 🌟
