import requests
import os


def get_chat_ids(token):
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(url)
    updates = response.json()

    chat_ids = []

    if 'result' in updates and len(updates['result']) > 0:
        for update in updates['result']:
            chat_id = update['message']['chat']['id']
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)
        return chat_ids
    else:
        raise Exception("No Chat-IDs Found!-")


'''
    @brief: Send The Message To All The Chat-Id Who're Accessing My ChatBot!-
    @credits: Telegram Chat Bot APIs
'''


def send_telegram_message(body):
    bot_token = os.getenv('TG_CHAT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': body}
    response = requests.post(url, data=payload)
    return response.status_code
