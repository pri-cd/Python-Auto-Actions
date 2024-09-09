import requests
import time
import os


def get_chat_ids_from_api(token):
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
        print("No Chat-IDs Found!-")
        return chat_ids


'''
    @brief: Send The Message To Only My Chat Id!
    @credits: Telegram Chat Bot APIs
'''


def send_telegram_message(body):
    bot_token = os.getenv('TG_CHAT_TOKEN')
    chat_ids = get_chat_ids_from_api(bot_token)
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    if len(chat_ids) < 1:
        print("No chat IDs available to send the message.")
        print("Sending To Only Pri!")

    chat_ids.append(os.getenv("TG_CHAT_ID"))
    print(f"Chat IDs- ALL: {chat_ids}")
    response = None

    # Removing Duplicates!-
    chat_ids = list(set(chat_ids))
    print(f"Chat IDs- FINAL!!!: {chat_ids}")

    print(" ============= Starting Send!=============== ")
    for chat_id in chat_ids:
        print(f"Sending message to chat ID: {chat_id}")
        payload = {'chat_id': chat_id, 'text': body}
        response = requests.post(url, data=payload)
        time.sleep(1)
    print(" ============= Ending Send!=============== ")

    return response.status_code if response else None
