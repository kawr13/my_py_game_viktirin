from datetime import datetime

all_messages = [] # список всех сообщений

def add_message(author, text=None, password=None):
    message_log = {
        'author': author,
        'text': text,
        'password': password,
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(message_log)

def print_messages(msg):
    print(f"[{msg['author']}]: {msg['text']} / {msg['time']}")

def print_all_messages():
    for message in all_messages:
        print(f"[{message['author']}]: {message['text']} / {message['time']}")

add_message('Маша', 'Привет')
add_message('Маша', 'Какой у тебя день?')
add_message('Алекс', 'Привет Маша')
add_message('Леша', 'Привет')
add_message('Леша', 'Какой у тебя день?')
add_message('Алекс', 'Привет Леша')
add_message('Маша', 'Вы бухать будете?')

print_all_messages()
print_messages(all_messages[0])

all_messages = []



# chat_dict = {
#
# }
#
# chat_dict['alex'] = ['Привет всем', 'Я тут новичек']
# chat_dict['Маша'] = ['Привет Саша', 'Я тоже новичек']
# print(chat_dict['alex'])
#
# print(chat_dict)
#
# for key, value in message_dict.items():
#     print(f'Сообщения поступают от {key}')
#     for msg in value:
#         print(f'Сообщение от {key}: {msg}. {time}')