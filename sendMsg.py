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
    chat_ids = get_chat_ids(bot_token)

    if not chat_ids:
        raise Exception("No chat IDs available to send the message.")

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    response = None  # Initialize the response variable

    print(" ============= Starting Send!=============== ")
    for chat_id in chat_ids:
        print(f"Sending message to chat ID: {chat_id}")
        payload = {'chat_id': chat_id, 'text': body}
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            print(f"Failed to send message to chat ID: {chat_id}")
    print(" ============= Ending Send!=============== ")

    return response.status_code if response else None
