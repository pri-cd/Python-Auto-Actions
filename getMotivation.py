import requests
import random
'''
    @brief: Gets A Random Quote From The Quotable API
    @credits: https://github.com/lukePeavey/quotable
'''


# In Case API doesn't work- Utilise other Ways!-
def get_predefined_quote():
    print("Using Predefined Quote Function")
    quotes_dict = {
        "The only way to do great work is to love what you do.":
        "Steve Jobs",
        "Life is what happens when you're busy making other plans.":
        "John Lennon",
        "The purpose of our lives is to be happy.":
        "Dalai Lama",
        "Get busy living or get busy dying.":
        "Stephen King",
        "You have within you right now, everything you need to deal with whatever the world can throw at you.":
        "Brian Tracy",
        "In the end, we will remember not the words of our enemies, but the silence of our friends.":
        "Martin Luther King Jr.",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.":
        "Ralph Waldo Emerson",
        "The best way to predict the future is to invent it.":
        "Alan Kay",
        "Life is either a daring adventure or nothing at all.":
        "Helen Keller",
        "Success usually comes to those who are too busy to be looking for it.":
        "Henry David Thoreau",
        "Don't watch the clock; do what it does. Keep going.":
        "Sam Levenson",
        "You only live once, but if you do it right, once is enough.":
        "Mae West",
        "The only limit to our realization of tomorrow is our doubts of today.":
        "Franklin D. Roosevelt",
        "Act as if what you do makes a difference. It does.":
        "William James",
        "To live is the rarest thing in the world. Most people exist, that is all.":
        "Oscar Wilde",
        "I have not failed. I've just found 10,000 ways that won't work.":
        "Thomas Edison",
        "The future belongs to those who believe in the beauty of their dreams.":
        "Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop.":
        "Confucius",
        "The only person you are destined to become is the person you decide to be.":
        "Ralph Waldo Emerson",
        "You miss 100% of the shots you don't take.":
        "Wayne Gretzky",
        "Whether you think you can or you think you can't, you're right.":
        "Henry Ford",
        "Everything you’ve ever wanted is on the other side of fear.":
        "George Addair",
        "Opportunities don't happen. You create them.":
        "Chris Grosser",
        "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.":
        "Roy T. Bennett",
        "Believe you can and you're halfway there.":
        "Theodore Roosevelt",
        "The only way to achieve the impossible is to believe it is possible.":
        "Charles Kingsleigh",
        "The harder I work, the luckier I get.":
        "Samuel Goldwyn",
        "Don't let yesterday take up too much of today.":
        "Will Rogers",
        "We may encounter many defeats but we must not be defeated.":
        "Maya Angelou",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.":
        "Nelson Mandela",
        "The way to get started is to quit talking and begin doing.":
        "Walt Disney",
        "Life is short, and it is up to you to make it sweet.":
        "Sarah Louise Delany",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.":
        "James Cameron",
        "You do not find the happy life. You make it.":
        "Camilla E. Kimball",
        "We are what we repeatedly do. Excellence, then, is not an act, but a habit.":
        "Aristotle",
        "Your time is limited, so don't waste it living someone else's life.":
        "Steve Jobs"
    }

    quote, author = random.choice(list(quotes_dict.items()))
    return quote, author


def get_motivation_quote():
    base_url = "https://api.quotable.io"
    path = '/quotes/random'
    complete_url = f"{base_url}{path}"

    params = {
        "maxLength": 300,
        "minLength": 100,
        "tags": "Sucess|Wisdom",
        "limit": 5
    }

    try:
        response = requests.get(complete_url, params=params)
        if response.status_code == 200:
            quotes = response.json()
            selected_quote = random.choice(quotes)
            return selected_quote['content'], selected_quote['author']
        else:
            return get_predefined_quote()
    except Exception as exp:
        print(f"Exception: {exp} Occured!")
        return get_predefined_quote()
