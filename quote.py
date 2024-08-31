import requests
import random

baseUrl = "https://api.quotable.io"


def getAuthors(url=baseUrl, path='/authors'):
    payload = {}
    headers = {}

    completeUrl = f"{url}{path}"
    print(completeUrl)
    params = {
        "sortBy": "name",
        "order": "asc",
        "slug": "",
        "limit": 20,
        "page": 1
    }

    return requests.request(method="GET",
                            url=completeUrl,
                            headers=headers,
                            params=params,
                            data=payload)


# Function to get a motivational quote
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


def getTags(url=baseUrl, path="/tags"):
    completeUrl = f"{url}{path}"
    print(completeUrl)
    payload = {}
    headers = {}

    params = {"sortBy": "name", "order": -1}
    return requests.request(method="GET",
                            url=completeUrl,
                            headers=headers,
                            params=params,
                            data=payload)
