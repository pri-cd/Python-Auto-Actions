import requests
import time
import os


def get_chat_ids_from_api(token):
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(url)
    updates = response.json()

    chat_ids = set()

    if 'result' in updates and len(updates['result']) > 0:
        for update in updates['result']:
            chat_id = update['message']['chat']['id']
            chat_ids.add(chat_id)
        return list(chat_ids)
    else:
        print("No Chat-IDs Found!")
        return []


'''
    @brief: Send The Message To Only My Chat Id!
    @credits: Telegram Chat Bot APIs
'''


def send_telegram_message(bodies):
    bot_token = os.getenv('TG_CHAT_TOKEN')
    chat_ids = get_chat_ids_from_api(bot_token)
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    if not chat_ids:
        print("No chat IDs available to send the message.")
        print("Sending To Only Pri!")
        chat_ids.append(os.getenv("TG_CHAT_ID"))

    # Convert to a set to remove any potential duplicates
    chat_ids = list(set(chat_ids))
    print(f"Chat IDs- FINAL: {chat_ids}")
    response = None
    print(">>>>>>>>>> Starting Send >>>>>>>>>>")
    for body in bodies:
        for chat_id in chat_ids:
            print(f"Sending message to chat ID: {chat_id}")
            payload = {'chat_id': chat_id, 'text': body}
            response = requests.post(url, data=payload)
            time.sleep(1)
    print(">>>>>>>>>> Ending Send >>>>>>>>>>")

    return response
