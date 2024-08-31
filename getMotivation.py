import requests
import random
'''
    @brief: Gets A Random Quote From The Quotable API
    @credits: https://github.com/lukePeavey/quotable
'''


def get_motivation_quote():
    base_url = "https://api.quotable.io"
    path = '/quotes/random'
    complete_url = f"{base_url}{path}"

    params = {
        "maxLength": 300,
        "minLength": 100,
        "tags": "Sucess|Technology|Wisdom",
        "limit": 5
    }

    response = requests.get(complete_url, params=params)
    quotes = response.json()
    selected_quote = random.choice(quotes)
    return selected_quote['content'], selected_quote['author']
